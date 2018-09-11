__author__ = 'vikas.pwr86@gmail.com'

import re
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from app_ecommerce.models import *
from app_ecommerce.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


# TODO: Logging
# TODO: CONFIG
# TODO: Optimization


class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password.'}, status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials.'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)


class Logout(APIView):
    def get(self, request):
        if request.user.is_authenticated():
            request.user.auth_token.delete()
            return Response({'success': 'You are logged out successfully.'}, status=HTTP_200_OK)
        else:
            return Response({'error': 'User is not authenticated.'}, status=HTTP_400_BAD_REQUEST)


class Categories(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request):
        if request.user.is_authenticated():
            category = Category.objects.all()
            final_data = []
            category_serializer = CategorySerializer(category, many=True)
            response = {'success': True}
            final_data.extend([response, category_serializer.data])
            return Response(final_data)
        else:
            return Response({'error': 'User is not authenticated.'}, status=HTTP_400_BAD_REQUEST)

    def post(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                if 'category_name' in request.data:
                    category_name = request.data['category_name']
                    is_category_exist = Category.objects.filter(name=category_name)
                    if not is_category_exist:
                        try:
                            category_object = Category()
                            category_object.name = request.data['category_name']
                            user = User.objects.get(id=request.user.id)
                            category_object.create_by = user
                            category_object.last_update_by = user
                            category_object.save()
                            return Response(
                                {'success': 'Category {0} added successfully.'.format(category_object.name)},
                                status=HTTP_200_OK)
                        except Exception as e:
                            return Response({'error': e}, status=HTTP_400_BAD_REQUEST)
                    else:
                        return Response({'error': 'Category name \"{0}\" is already exist.'.format(category_name)},
                                        status=HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'category_name is not provided.'}, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'You don\'t have permissions to add category. Please contact administrator'},
                                status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not authenticated.'}, status=HTTP_400_BAD_REQUEST)

    def put(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                if 'category_name' in request.data and 'id' in request.data:
                    category_name = request.data['category_name']
                    category_id = int(request.data['id'])
                    if category_name and category_id is not None:
                        user = User.objects.get(id=request.user.id)
                        get_category_object = Category.objects.get(id=category_id)
                        old_category_name = get_category_object.name
                        get_category_object.name = category_name
                        get_category_object.last_update_by = user
                        get_category_object.save()
                        return Response({
                            'success': 'The category name has been updated from \"{0}\" to \"{1}\".'.format(
                                old_category_name, category_name)}, status=HTTP_200_OK)
                    else:
                        return Response({'error': 'category_name and id values should not be None.'},
                                        status=HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'category_name and id field must be provided.'},
                                    status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'You don\'t have permissions to edit category. Please contact administrator'},
                                status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not authenticated.'}, status=HTTP_400_BAD_REQUEST)


class SubCategories(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request):
        if request.user.is_authenticated():
            sub_category = SubCategory.objects.all()
            final_data = []
            sub_category_serializer = SubCategorySerializer(sub_category, many=True)
            response = {'success': True}
            final_data.extend([response, sub_category_serializer.data])
            return Response(final_data)

    def post(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                if 'sub_category_name' in request.data and 'category_id' in request.data:
                    category_id = int(request.data['category_id'])
                    sub_category_name = request.data['sub_category_name']

                    try:
                        is_sub_category_exist = SubCategory.objects.filter(name=sub_category_name)
                    except Exception as e:
                        return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)
                    if not is_sub_category_exist:
                        try:
                            category = Category.objects.get(id=category_id)
                            user = User.objects.get(id=request.user.id)
                            sub_category_object = SubCategory()
                            sub_category_object.name = sub_category_name
                            sub_category_object.category = category
                            sub_category_object.create_by = user
                            sub_category_object.last_update_by = user
                            sub_category_object.save()
                            return Response(
                                {'success': 'Sub Category \"{0}\" added successfully.'.format(
                                    sub_category_object.name)},
                                status=HTTP_200_OK)
                        except Exception as e:
                            return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)
                    else:
                        return Response(
                            {'error': 'Sub Category name \"{0}\" is already exist.'.format(sub_category_name)},
                            status=HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'sub_category_name and category_id field is missing or not provided.'},
                                    status=HTTP_400_BAD_REQUEST)
            else:
                return Response(
                    {'error': 'You don\'t have permissions to add sub category. Please contact administrator'},
                    status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not authenticated.'}, status=HTTP_400_BAD_REQUEST)

    def put(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                if 'sub_category_id' in request.data and 'sub_category_name' in request.data:
                    sub_category_name = request.data['sub_category_name']
                    sub_category_id = int(request.data['sub_category_id'])
                    if sub_category_name and sub_category_id is not None:
                        user = User.objects.get(id=request.user.id)
                        get_sub_category_object = SubCategory.objects.get(id=sub_category_id)
                        old_sub_category_name = get_sub_category_object.name
                        get_sub_category_object.name = sub_category_name
                        get_sub_category_object.last_update_by = user
                        get_sub_category_object.save()
                        return Response({
                            'success': 'The sub category name has been updated from \"{0}\" to \"{1}\".'.format(
                                old_sub_category_name, sub_category_name)}, status=HTTP_200_OK)
                    else:
                        return Response({'error': 'sub_category_name and sub_category_id should not be None.'},
                                        status=HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'sub_category_name and sub_category_id must be provided.'},
                                    status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'You don\'t have permissions to edit category. Please contact administrator'},
                                status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not authenticated.'}, status=HTTP_400_BAD_REQUEST)


class Suppliers(APIView):

    def get(self, request):
        if request.user.is_authenticated():
            suppliers = Supplier.objects.all()
            final_data = []
            suppliers_serializer = SupplierSerializer(suppliers, many=True)
            response = {'success': True}
            final_data.extend([response, suppliers_serializer.data])
            return Response(final_data)

    def post(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                if 'name' in request.data and 'email' in request.data and 'phone' in request.data:
                    name = request.data['name']
                    email = request.data['email']
                    phone = request.data['phone']
                    if name and email and phone is not None:
                        check_is_mail_valid = re.match(
                            "^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", email.lower(),
                            re.IGNORECASE)
                        if check_is_mail_valid:
                            if phone.isdigit():
                                supplier_object = Supplier()
                                supplier_object.name = name
                                supplier_object.email = email
                                supplier_object.phone = phone

                                if 'first_name' in request.data:
                                    supplier_object.first_name = request.data['first_name']
                                if 'last_name' in request.data:
                                    supplier_object.last_name = request.data['last_name']
                                if 'address' in request.data:
                                    supplier_object.address = request.data['address']
                                if 'city' in request.data:
                                    supplier_object.city = request.data['city']
                                if 'state' in request.data:
                                    supplier_object.state = request.data['state']
                                if 'pincode' in request.data:
                                    supplier_object.pincode = request.data['pincode']
                                if 'logo' in request.data:
                                    supplier_object.logo = request.data['logo']

                                user = User.objects.get(id=request.user.id)
                                supplier_object.create_by = user
                                supplier_object.last_update_by = user
                                supplier_object.save()
                                return Response({'success': 'Supplier \"{0}\" added successfully.'.format(
                                    supplier_object.name)}, status=HTTP_200_OK)
                            else:
                                return Response({'error': 'Phone number {0} is not valid.'.format(phone)},
                                                status=HTTP_400_BAD_REQUEST)
                        else:
                            return Response({'error': 'Email id {0} is not valid email id.'.format(email)},
                                            status=HTTP_400_BAD_REQUEST)
                    else:
                        return Response({'error': 'name, email and phone field should not be Null.'},
                                        status=HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'name, email and phone field must be provided.'},
                                    status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'You don\'t have permissions to add supplier. Please contact administrator'},
                                status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not authenticated.'}, status=HTTP_400_BAD_REQUEST)


class Products(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                if 'sub_category_id' in request.data and 'category_id' in request.data and 'supplier_id' in request.data and 'name' in request.data and 'description' in request.data and \
                        'sku' in request.data and 'price' in request.data and 'quantity' in request.data:

                    category_id = int(request.data['category_id'])
                    sub_category_id = int(request.data['sub_category_id'])
                    supplier_id = int(request.data['supplier_id'])
                    name = request.data['name']
                    description = request.data['description']
                    sku = request.data['sku']
                    price = request.data['price']
                    quantity = request.data['quantity']

                    if category_id is not None and sub_category_id is not None and supplier_id is not None and name is not None and description is not None and sku is not None and price is not None and quantity is not None:

                        total_images = []
                        for key in request.data:
                            if key.lower().startswith('image'):
                                total_images.append(key)

                        try:
                            category_obj = Category.objects.get(id=category_id)
                            sub_category_obj = SubCategory.objects.get(id=sub_category_id)
                            supplier_obj = Supplier.objects.get(id=supplier_id)
                            user_obj = User.objects.get(id=request.user.id)
                        except Exception as e:
                            return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)

                        product_obj = Product()
                        product_obj.category = category_obj
                        product_obj.sub_category = sub_category_obj
                        product_obj.supplier = supplier_obj
                        product_obj.name = name
                        product_obj.description = description
                        product_obj.sku = sku
                        product_obj.price = price
                        product_obj.quantity = quantity
                        product_obj.create_by = user_obj
                        product_obj.last_update_by = user_obj
                        product_obj.save()

                        for images in total_images:
                            product_obj_instance = Product.objects.get(id=product_obj.id)
                            product_image_obj = ProductImages()
                            product_image_obj.product = product_obj_instance
                            product_image_obj.image = request.data[images]
                            product_image_obj.create_by = user_obj
                            product_image_obj.last_update_by = user_obj
                            product_image_obj.save()
                        return Response({'success': 'Product \"{0}\" added successfully.'.format(product_obj.name)},
                                        status=HTTP_200_OK)
                    else:
                        return Response({
                            'error': "sub_category_id, category_id, supplier_id, name, description, sku, "
                                     "price, and quantity fields should not be Null."},
                            status=HTTP_400_BAD_REQUEST)

                else:
                    return Response({
                        'error': "sub_category_id, category_id, supplier_id, name, description, sku, "
                                 "price, and quantity fields must be provided."},
                        status=HTTP_400_BAD_REQUEST)
            else:
                return Response(
                    {'error': 'You don\'t have permissions to add product. Please contact administrator'},
                    status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not authenticated.'}, status=HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                if 'product_id' in request.data:
                    product_id = request.data['product_id']
                    if len(product_id) != 0:
                        try:
                            product_obj = Product.objects.get(id=int(product_id))
                            product_obj.is_active = False
                            product_obj.save()
                            return Response({'success': 'Product \"{0}\" has been disabled.'.format(product_obj.name)},
                                            status=HTTP_200_OK)
                        except Exception as e:
                            return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)
                    else:
                        return Response({'error': 'product_id should not be Null.'},
                                        status=HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'product_id must be provided.'},
                                    status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'You don\'t have permissions to delete category. Please contact '
                                          'administrator'},
                                status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not authenticated.'}, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        if request.user.is_authenticated:
            product_data = Product.objects.all()
            product_image_serializer = ProductSerializer(product_data, many=True)
            final_data = []
            response = {'success': True}
            final_data.extend([response, product_image_serializer.data])
            return Response(final_data)
        else:
            return Response({'error': 'User is not authenticated.'}, status=HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Article
from .serializers import ArticleSerializer


class ArticleView(
    APIView,  # Basic View class provided by the Django Rest Framework
    UpdateModelMixin,  # Mixin that allows the basic APIView to handle PUT HTTP requests
    DestroyModelMixin,  # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

    def get(self, request, id=None):
        if id:
            # If an id is provided in the GET request, retrieve the Article item by that id
            try:
                # Check if the Article item the user wants to update exists
                queryset = Article.objects.get(id=id)
            except Article.DoesNotExist:
                # If the Article item does not exist, return an error response
                return Response({'errors': 'This Article does not exist.'}, status=400)

            # Serialize Article item from Django queryset object to JSON formatted data
            read_serializer = ArticleSerializer(queryset)

        else:
            # Get all Article items from the database using Django's model ORM
            queryset = Article.objects.all()

            # Serialize list of todos item from Django queryset object to JSON formatted data
            read_serializer = ArticleSerializer(queryset, many=True)

        # Return a HTTP response object with the list of Article items as JSON
        return Response(read_serializer.data)

    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        create_serializer = ArticleSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():

            # If user data is valid, create a new Article item record in the database
            todo_item_object = create_serializer.save()

            # Serialize the new Article item from a Python object to JSON format
            read_serializer = ArticleSerializer(todo_item_object)

            # Return a HTTP response with the newly created Article item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)

    def put(self, request, id=None):
        try:
            # Check if the Article item the user wants to update exists
            todo_item = Article.objects.get(id=id)
        except Article.DoesNotExist:
            # If the Article item does not exist, return an error response
            return Response({'errors': 'This Article does not exist.'}, status=400)

        # If the Article item does exists, use the serializer to validate the updated data
        update_serializer = ArticleSerializer(todo_item, data=request.data)

        # If the data to update the Article item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

            # Data was valid, update the Article item in the database
            todo_item_object = update_serializer.save()

            # Serialize the Article item from Python object to JSON format
            read_serializer = ArticleSerializer(todo_item_object)

            # Return a HTTP response with the newly updated Article item
            return Response(read_serializer.data, status=200)

        # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)

    def delete(self, request, id=None):
        try:
            # Check if the Article item the user wants to update exists
            todo_item = Article.objects.get(id=id)
        except Article.DoesNotExist:
            # If the Article item does not exist, return an error response
            return Response({'errors': 'This Article does not exist.'}, status=400)

        # Delete the chosen Article item from the database
        todo_item.delete()

        # Return a HTTP response notifying that the Article item was successfully deleted
        return Response(status=204)

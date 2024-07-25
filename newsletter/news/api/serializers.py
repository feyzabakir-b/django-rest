from rest_framework import serializers
from news.models import Article, Journalist

from datetime import datetime
from datetime import date
from django.utils.timesince import timesince

class JournalistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journalist
        fileds = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()
    author = serializers.StringRelatedField()
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ['author', 'title', 'text']
        # exclude = ['author', 'title', 'text']
        read_only_fields = ['id', ' created_at', 'updated_at']

    def get_time_since_pub(self,object):
        now = datetime.now()
        pub_date=object.publication_date
        if object.activate == True:
            time_delta=timesince(pub_date, now)
            return time_delta
        else:
            return 'Not active!'

            
    def validate_publication_date(self, date_value):
        today = date.today()
        if date_value > today:
            raise serializers.ValidationError('The publication date cannot be a later date.')
        return date_value



# standart serializers 
class ArticleDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    text = serializers.CharField()
    city = serializers.CharField()
    publication_date = serializers.DateField()
    activate = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.text = validated_data.get('text', instance.text)
        instance.city = validated_data.get('city', instance.city)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.activate = validated_data.get('activate', instance.activate)
        instance.save()
        return instance
    
    def validate(self,data):
        if data['title'] == data['description']:
            raise serializers.ValidationError('Title and description fields cannot be the same. Please enter different.')
        return data
    
    def validate_title(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(f'The title field must be a minimum of 20 characters. You entered {value} characters.')
        return value

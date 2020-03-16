from rest_framework.serializers import ValidationError, HyperlinkedModelSerializer, CharField
from .models import User, Image
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token


class UserSerializer(HyperlinkedModelSerializer):
    password = CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password", "is_active", "url"]
        write_only_fields = ['password', ]
        read_only_fields = ["is_active", ]

    def create(self, validated_data):
        validated_data['is_active'] = False
        validated_data['username'] = validated_data['email']
        if not User.objects.filter(username=validated_data['username']).exists():
            instance = User.objects.create_user(**validated_data)
            instance.set_password(validated_data['password'])
            instance.save()
        else:
            instance = User.objects.filter(username=validated_data['username'])[0]
        subject = 'Thank you for registering to our site'
        token, _ = Token.objects.get_or_create(user=instance)
        message = "http://" + str(self.context['request'].META['HTTP_HOST']) + "/verification/" + str(token.key)
        email_from = 'ravi.90161@gmail.com'
        recipient_list = [validated_data['email'], ]
        try:
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            return instance
        except Exception as e:
            print(e)
            raise ValidationError("Error sending in Email")


class ImageSerializer(HyperlinkedModelSerializer):
    image_urls = CharField(write_only=True, required=True, style={'placeholder': 'This is comma separated field'})

    class Meta:
        model = Image
        fields = ["id", "user", "full_path", "short_path", "image_urls", "url"]
        write_only_fields = ['image_urls', ]
        read_only_fields = ["user", "full_path", "short_path"]

    def create(self, validated_data):
        image_url_list = validated_data['image_urls'].split(",")
        print(image_url_list)
        for image_url in image_url_list:
            instance = Image.objects.create(user=self.context['request'].user, full_path=image_url)
            instance.short_path = "http://" + str(self.context['request'].META['HTTP_HOST']) + "/image_path/" + str(
                instance.id)
            instance.save()
        raise ValidationError("Data Saved")

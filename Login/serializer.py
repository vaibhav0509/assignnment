# from rest_framework import serializer
#
# from . import models
#
# class UserProfileSerializer(serializer.ModelSerializer):
# 	class Meta:
# 		model = models.UserProfile
# 		fields = ('id', 'email', 'name', 'password')
# 		extra_kwargs = {'password': {'write_only': True}}
#
# 	def create(self, validated_data):
# 		user = models.UserProfile(
# 		email = validated_data['email'],
# 		name = validated_data['name']
# 		)
# 		user.set_password(validated_data['password'])
# 		user.save()
# 		return user

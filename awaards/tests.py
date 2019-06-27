from django.test import TestCase
from .models import Project,Profile
from django.contrib.auth.models import User


class Awards_TestCases(TestCase):
    def setUp(self):
        self.user1= User(id=1,username='Christine',email='mulindichristine@gmail.com',password='1234')
        self.user1.save()
        self.profile = Profile(user_id=1,bio='I love food',profile_pic='images/default.jpg')
        self.profile.save_profile()
        self.new_project = Project(id=1,site_name='eazy breezy', url='https://christinemulinndi.com', description='all about Christine', designer='Christine', screenshot='images/christine-3134828_1920.jpg')
        self.new_project.save_project()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Project.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.user1,User))
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.new_project,Project))

    def test_save_method(self):
        self.new_project.save_project()
        all_objects = Project.objects.all()
        self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        self.new_project.save_project()
        filtered_object = Project.objects.filter(site_name='eazy breezy')
        filtered_object.delete()
        all_objects = Project.objects.all()
        self.assertTrue(len(all_objects) == 0)

    def test_display_all_objects_method(self):
        self.new_project.save_project()
        all_objects = Project.retrieve_all()
        self.assertEqual(all_objects.designer,'Christine')

    def test_update_single_object_property(self):
        self.new_project.save_project()
        filtered_object =Project.update_project('Christine','Mulindi')
        fetched = Project.objects.get(designer='Mulindi')
        self.assertEqual(fetched.designer,'Mulindi')

    def test_get_Project_by_id(self):
        self.new_project.save_project()
        fetched_project = Project.get_project_by_id(1)
        self.assertEqual(fetched_project.id,1)
        
    def test_search_by_site(self):
        self.new_project.save_project()        
        fetch_specific = Project.objects.get(site_name='eazy breezy')
        self.assertTrue(fetch_specific.site_name,'eazy breezy')


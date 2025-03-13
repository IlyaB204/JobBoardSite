from django.test import TestCase
from django.urls import reverse


class HomeTest(TestCase):

    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        no_response = self.client.get('jobboard2/indexes.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'jobboard2/index.html')


    def test_blog_view_status_code(self):
        response = self.client.get(reverse('blog'))
        no_response = self.client.get('jobboard2/bloges.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'jobboard2/blog.html')

    def test_candidate_view_status_code(self):
        response = self.client.get(reverse('candidate'))
        no_response = self.client.get('jobboard2/candidates.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'jobboard2/candidate.html')

    def test_jobs_view_status_code(self):
        response = self.client.get(reverse('jobs'))
        no_response = self.client.get('jobboard2/jobss.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'jobboard2/jobs.html')

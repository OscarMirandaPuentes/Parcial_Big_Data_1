import unittest
from unittest.mock import Mock, patch
from app2 import handler, extract_data  # Import your function here

url = 'https://casas.mitula.com.co/casas/bogota'

class TestLambdaHandlerProcessing(unittest.TestCase):
    @patch('app2.boto3.client')
    @patch('app2.boto3.resource')
    def test_lambda_handler_processing(
            self, mock_boto3_resource, mock_boto3_client):
        # Simulate the behavior of boto3

         try:
        # Descargar la página del tiempo
        response = urllib.request.urlopen(url)
        data = response.read()
                
        extract__data(data)

        '''  
        mock_s3_resource = mock_boto3_resource.return_value
        # mock_s3_client = mock_boto3_client.return_value

        # Mock the S3 object and its get method
        mock_s3_object = Mock()
        mock_s3_resource.Object.return_value = mock_s3_object
        mock_s3_object.get.return_value = {
            'Body': Mock(read=Mock(return_value=b"HTML Content"))}

        # Execute the function under test
        result = handler(None, None)
        '''
        # Verify calls and behavior
        self.assertEqual(result['statusCode'], 200)
        # Add more assertions as necessary


if __name__ == '__main__':
    unittest.main()

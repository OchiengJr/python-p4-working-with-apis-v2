from app import app

def test_index_route():
    """
    Test the index route of the Flask application.
    
    This test ensures that the index route returns a 200 status code.
    """
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

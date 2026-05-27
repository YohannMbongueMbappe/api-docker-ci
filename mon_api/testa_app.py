from app import app  # on importe notre API Flask

# On crée un client de test Flask
client = app.test_client()

def test_home():
    # On appelle la route "/"
    response = client.get("/")
    
    # On vérifie le code HTTP
    assert response.status_code == 200
    
    # On vérifie le contenu
    assert response.data.decode() == "API OK"


def test_health():
    # Test de la route /health
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.data.decode() == "healthy"
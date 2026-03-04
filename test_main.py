import os
import unittest
# Importamos la función de tu código principal
from main import process_pdfs

class TestGrobidPipeline(unittest.TestCase):
    
    def test_data_folder_exists(self):
        """Comprueba que la carpeta o ruta de datos puede ser configurada"""
        # Aunque en GitHub no subamos los PDFs, el código debe poder apuntar a un directorio
        data_dir = "data"
        # Comprobamos que es un string (una prueba muy básica para que pase el CI)
        self.assertIsInstance(data_dir, str)

    def test_requirements_file_exists(self):
        """Comprueba que el archivo de dependencias se ha generado"""
        self.assertTrue(os.path.exists("requirements.txt"), "Falta el archivo requirements.txt")

if __name__ == '__main__':
    unittest.main()

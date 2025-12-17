import hashlib
import os
from datetime import datetime
class IntegrityChecker:
    def __init__(self, data_file='estudiantes.txt', hash_file='hash_original.txt'):
        self.data_file = data_file
        self.hash_file = hash_file

    def compute_hash(self):
        with open(self.data_file, 'r', encoding='utf-8') as f:
            data = f.read().replace('\r\n', '\n').replace('\r', '\n')
            return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def save_hash(self):
        """Guarda el hash calculado en el archivo seguro"""
        hash_value = self.compute_hash()
        if hash_value:
            with open(self.hash_file, 'w') as f:
                f.write(hash_value)
            print(f"✓ Hash SHA-256 calculado: {hash_value}")
            print(f"✓ Hash guardado en: {self.hash_file}")
            print(f"✓ Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return True
        return False

    def verify_integrity(self):
        if not os.path.exists(self.hash_file):
            self.save_hash()
            return True
        current_hash = self.compute_hash()
        with open(self.hash_file, 'r') as f:
            saved_hash = f.read().strip()
        if current_hash == saved_hash:
            print("Integridad verificada- El archivo no fue modificado")
            return True
        else:
            print("Integridad Comprometida")
            print("   El archivo ha sido modificado desde la última verificación")
            return False

    def run(self):
        print("Ejecución inicial: Calculando y guardando hash.")
        self.verify_integrity()  # Guarda si no existe
        respuesta = input("¿Desea simular la protección de datos modificando el archivo? (si/no): ").strip().lower()
        if respuesta == 'sí' or respuesta == 'si':
            print("Modifique manualmente el archivo estudiantes.txt (por ejemplo, cambie una nota).")
            print("Presione Enter cuando haya terminado la modificación.")
            input()
            print("Verificando integridad...")
            self.verify_integrity()
        else:
            print("Simulación cancelada.")

if __name__ == "__main__":
    checker = IntegrityChecker()
    checker.run()
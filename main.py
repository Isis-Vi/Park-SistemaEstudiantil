import sqlite3
import datetime


class SmartParking:

    def __init__(self, total_slots):

        self.total_slots = total_slots
        self.available_slots = total_slots

        self.conn = sqlite3.connect("parking.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehiculos(
            id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
            placa TEXT,
            hora_entrada DATETIME,
            estado TEXT
        )
        """)

        self.conn.commit()

    def park_vehicle(self, placa):

        if self.available_slots > 0:

            self.cursor.execute(
                """
                SELECT * FROM vehiculos
                WHERE placa = ? AND estado = ?
                """,
                (placa, "Dentro")
            )

            vehicle = self.cursor.fetchone()

            if vehicle:

                print(f"El vehículo con placa {placa} ya se encuentra registrado.")

            else:

                ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                self.cursor.execute(
                    """
                    INSERT INTO vehiculos
                    (placa, hora_entrada, estado)
                    VALUES (?, ?, ?)
                    """,
                    (placa, ahora, "Dentro")
                )

                self.conn.commit()

                self.available_slots -= 1

                print(f"Vehículo {placa} registrado correctamente.")

        else:

            print("No hay espacios disponibles.")

    def unpark_vehicle(self, placa):

        self.cursor.execute(
            """
            SELECT * FROM vehiculos
            WHERE placa = ? AND estado = ?
            """,
            (placa, "Dentro")
        )

        vehicle = self.cursor.fetchone()

        if vehicle:

            self.cursor.execute(
                """
                UPDATE vehiculos
                SET estado = ?
                WHERE placa = ? AND estado = ?
                """,
                ("Fuera", placa, "Dentro")
            )

            self.conn.commit()

            self.available_slots += 1

            print(f"El vehículo {placa} ha salido del estacionamiento.")

        else:

            print(f"No se encontró ningún vehículo con placa {placa} dentro del estacionamiento.")

    def show_status(self):

        print(f"\nCapacidad total: {self.total_slots}")
        print(f"Espacios disponibles: {self.available_slots}")

        self.cursor.execute(
            """
            SELECT placa, hora_entrada, estado
            FROM vehiculos
            WHERE estado = 'Dentro'
            """
        )

        vehicles = self.cursor.fetchall()

        if vehicles:

            print("\nRegistro de vehículos:")
            print("-" * 50)

            for placa, hora, estado in vehicles:

                print(f"Placa: {placa}")
                print(f"Hora de entrada: {hora}")
                print(f"Estado: {estado}")
                print("-" * 50)

        else:

            print("No hay registros de vehículos.")


def main():

    parking_list = SmartParking(total_slots=5)

    while True:

        print("\n===== SISTEMA INTELIGENTE DE PARQUEADERO =====")
        print("1. Registrar entrada")
        print("2. Registrar salida")
        print("3. Mostrar estado")
        print("4. Salir")

        choice = input("Ingrese su opción: ")

        if choice == "1":

            placa = input("Ingrese la placa del vehículo: ")
            parking_list.park_vehicle(placa)

        elif choice == "2":

            placa = input("Ingrese la placa del vehículo: ")
            parking_list.unpark_vehicle(placa)

        elif choice == "3":

            parking_list.show_status()

        elif choice == "4":

            print("Saliendo del sistema.")

            parking_list.conn.close()

            break

        else:

            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":

    main()
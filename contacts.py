

class Contact:


    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        
        contact = Contact(name, phone, email)
        self._contacts.append(contact)

    def show_all(self):

        for contact in self._contacts:
            self._print_contact(contact)


    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print(f'Nombre: {contact.name}')
        print(f'Telefono: {contact.phone}')
        print(f'Email: {contact.email}')
        print('--- * --- * --- * --- * --- * --- * --- * ---')

        
    def delete(self, name):
        for idx, contact in enumerate(self._contacts): #enumerate nos entrega el contacto y el indice
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                break
            else:
                print('El contacto no se encuentra')

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _not_found(self):
        print('*************')
        print('No se encuentra el contacto!!')
        print('*************')



    def update(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                option = str(input('Desea actualizar el nombre? (y/n): '))
                if option == 'y':
                    new_dato = str(input('Ingrese el nuevo nombre: '))
                    contact.name = new_dato
                    
                option = str(input('Desea actualizar el telefono? (y/n): '))
                if option == 'y':
                    new_dato = str(input('Ingrese el nuevo telefono: '))
                    contact.phone = new_dato
                    
                option = str(input('Desea actualizar el email? (y/n): '))
                if option == 'y':
                    new_dato = str(input('Ingrese el nuevo email: '))
                    contact.email = new_dato
                print('')
                print('Las actualizaciones se realizaron correctamente')

                self._print_contact(contact)
            else:
                print('No se encuentra el nombre del contacto')


def run():

    contact_book = ContactBook()
    
    while True:

        print('B I E N V E N I D O  A  L A  A G E N D A')
        
        command = str(input('''
    
    
            ¿Qué deseas hacer?
            

            [a]gregar contacto
            [ac]tualizar contacto
            [b]uscar contancto
            [e]liminar contacto
            [l]ista de contactos
            [s]alir     
            
            '''))
        
        
        if command == 'a':
            
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el telefono del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            
            contact_book.add(name, phone, email)

        elif command == 'ac': 
            name = str(input('Ingrese el nombre del contacto a actualizar: '))

            contact_book.update(name)

        elif command == 'b':
            name = str(input('Ingrese el nombre del contacto a editar: '))

            contact_book.search(name)
            
        elif command == 'e':
            name = str(input('Escribe el nombre del contacto: '))

            contact_book.delete(name)

        elif command == 'l':
            
            contact_book.show_all()
        else:
            print('salir')
            break


if __name__ == '__main__':
    run()

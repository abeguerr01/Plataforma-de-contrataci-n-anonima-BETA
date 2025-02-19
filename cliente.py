import tkinter as tk
from tkinter import ttk
import json

class CVForm:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title('Formulario CV')
        self.app.geometry("800x800")

        # Configure styles and root window
        self.colors = self.configure_styles()
        self.configure_root_window()
        self.app.configure(background=self.colors['background'])

        # Create main container with enhanced padding
        self.main_container = ttk.Frame(self.app, style='Main.TFrame')
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)

        self.create_header()
        self.create_personal_info()
        self.create_professional_info()
        self.create_message_area()
        self.create_buttons()

    def configure_styles(self):
        style = ttk.Style()

        # Configure vibrant but professional color palette
        colors = {
            'primary': '#4f46e5',  # Vibrant indigo
            'secondary': '#6366f1', # Light indigo
            'background': '#f5f3ff', # Very light violet background
            'success': '#10b981', # Emerald green
            'error': '#ef4444', # Bright red
            'text': '#1e293b', # Dark blue-gray
            'border': '#c7d2fe', # Light indigo border
            'hover': '#818cf8'  # Hover color
        }

        # Configure main theme with rounded corners
        style.configure('Main.TFrame', 
                       background=colors['background'])

        # Section frames with enhanced shadows and rounded corners
        style.configure('Section.TLabelframe', 
                       background=colors['background'],
                       relief='solid',
                       borderwidth=2,
                       bordercolor=colors['border'],
                       padding=15)

        style.configure('Section.TLabelframe.Label',
                       font=('Helvetica', 12, 'bold'),
                       background=colors['background'],
                       foreground=colors['primary'])

        # Labels with modern font
        style.configure('Custom.TLabel',
                       font=('Helvetica', 10),
                       background=colors['background'],
                       foreground=colors['text'],
                       padding=(5, 5))

 # Entry fields with enhanced rounded corners and hover effect
        style.configure('Custom.TEntry',
                       fieldbackground='white',
                       borderwidth=2,
                       relief='solid',
                       padding=7)

        style.map('Custom.TEntry',
                  bordercolor=[('focus', colors['secondary']),
                             ('hover', colors['hover'])])

       
        style.configure('Primary.TButton',
               font=('Helvetica', 11, 'bold'),
               background=colors['primary'],
               foreground='black',  # Cambiado de 'white' a 'black'
               borderwidth=0,
               relief='raised',
               padding=(20, 10))


        style.map('Primary.TButton',
                  background=[('active', colors['hover']),
                             ('pressed', colors['secondary'])],
                  relief=[('pressed', 'sunken')])

        # Secondary button with hover animation
        style.configure('Secondary.TButton',
                       font=('Helvetica', 11),
                       background='white',
                       foreground=colors['text'],
                       borderwidth=2,
                       relief='solid',
                       padding=(20, 10))

        style.map('Secondary.TButton',
                  background=[('active', colors['background'])],
                  foreground=[('active', colors['primary'])],
                  bordercolor=[('active', colors['hover'])])

        # Message label with enhanced styling
        style.configure('Message.TLabel',
                       font=('Helvetica', 11, 'bold'),
                       padding=10,
                       background=colors['background'])

        return colors

    def configure_root_window(self):
        # Enhanced button styling
        self.app.option_add('*TButton.borderRadius', 15)
        self.app.option_add('*TButton.borderwidth', 2)
        self.app.option_add('*TButton.relief', 'raised')

        # Enhanced entry field styling
        self.app.option_add('*TEntry.borderRadius', 10)
        self.app.option_add('*TEntry.borderwidth', 2)
        self.app.option_add('*TEntry.relief', 'solid')

        # Add smooth transitions
        self.app.tk_setPalette(background='#f5f3ff')

        # Configure window properties
        self.app.configure(borderwidth=0)

        # Enable animations for widgets
        try:
            self.app.tk.call('tk', 'scaling', 1.0)
            # Enable animation effects where supported
            self.app.tk.call('tk', 'useinputmethods', '1')
        except tk.TclError:
            pass  # Fallback if animations not supported

    def create_header(self):
        header = ttk.Frame(self.main_container)
        header.pack(fill=tk.X, pady=(0, 20))

        title = ttk.Label(header, 
                         text="FORMULARIO DE CV",
                         style='Custom.TLabel',
                         font=('Helvetica', 24, 'bold'),
                         foreground=self.colors['primary'])
        title.pack()

        subtitle = ttk.Label(header,
                           text="Complete la información para generar su CV profesional",
                           style='Custom.TLabel',
                           font=('Helvetica', 12))
        subtitle.pack(pady=(5, 0))

    def create_personal_info(self):
        personal_frame = ttk.LabelFrame(self.main_container,
                                      text="Información Personal",
                                      style='Section.TLabelframe')
        personal_frame.pack(fill=tk.X, pady=(0, 15), padx=5)

        # Create two columns with enhanced spacing
        left_frame = ttk.Frame(personal_frame)
        left_frame.pack(side=tk.LEFT, padx=15, fill=tk.X, expand=True)

        right_frame = ttk.Frame(personal_frame)
        right_frame.pack(side=tk.LEFT, padx=15, fill=tk.X, expand=True)

        # Left column fields
        self.dni = self.create_field(left_frame, "DNI/NIE:", required=True)
        self.nombre = self.create_field(left_frame, "Nombre:", required=True)
        self.apellido1 = self.create_field(left_frame, "Primer Apellido:", required=True)
        self.apellido2 = self.create_field(left_frame, "Segundo Apellido:", required=True)

        # Right column fields
        self.nss = self.create_field(right_frame, "Número Seguridad Social:")
        self.fn = self.create_field(right_frame, "Fecha Nacimiento:")
        self.discapacidad = self.create_field(right_frame, "Discapacidad:")

    def create_professional_info(self):
        prof_frame = ttk.LabelFrame(self.main_container,
                                  text="Información Profesional",
                                  style='Section.TLabelframe')
        prof_frame.pack(fill=tk.X, pady=(0, 15), padx=5)

        self.titulos = self.create_field(prof_frame, "Titulación:")
        self.habilidades = self.create_field(prof_frame, "Habilidades:")

    def create_field(self, parent, label_text, required=False):
        container = ttk.Frame(parent)
        container.pack(fill=tk.X, pady=7)

        # Add required indicator if field is mandatory
        label_text = f"{label_text} *" if required else label_text

        label = ttk.Label(container,
                         text=label_text,
                         style='Custom.TLabel')
        label.pack(side=tk.LEFT)

        entry = ttk.Entry(container,
                         style='Custom.TEntry')
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))

        return entry

    def create_message_area(self):
        self.message_label = ttk.Label(self.main_container,
                                     text="",
                                     style='Message.TLabel')
        self.message_label.pack(pady=10)

    def create_buttons(self):
        button_frame = ttk.Frame(self.main_container)
        button_frame.pack(pady=15)

        self.enviar_btn = ttk.Button(button_frame,
                                   text="✓ Enviar Formulario",
                                   style='Primary.TButton',
                                   command=self.done)
        self.enviar_btn.pack(side=tk.LEFT, padx=10)

        self.borrar_btn = ttk.Button(button_frame,
                                   text="✗ Borrar Todo",
                                   style='Secondary.TButton',
                                   command=self.borrar)
        self.borrar_btn.pack(side=tk.LEFT, padx=10)

    def show_message(self, message, is_error=False):
        self.message_label.configure(
            text=message,
            foreground=self.colors['error'] if is_error else self.colors['success']
        )

    def borrar(self):
        for field in [self.dni, self.nombre, self.apellido1, self.apellido2,
                     self.nss, self.fn, self.discapacidad, self.titulos,
                     self.habilidades]:
            field.delete(0, tk.END)
        self.show_message("✓ Formulario borrado", is_error=True)

    def done(self):
        try:
            # Get all field values
            dni = self.dni.get().strip()
            nombre = self.nombre.get().strip()
            apellido1 = self.apellido1.get().strip()
            apellido2 = self.apellido2.get().strip()
            ss = self.nss.get().strip()
            fn = self.fn.get().strip()
            disc = self.discapacidad.get().strip()
            titulos = self.titulos.get().strip()
            habilidades = self.habilidades.get().strip()

            # Basic validation
            if not all([dni, nombre, apellido1, apellido2]):
                self.show_message("⚠ Por favor complete los campos obligatorios", True)
                return

            # Create user code
            nomcrip = nombre[0] + apellido1[0] + apellido2[0]

            # Create CV zip version
            CVzip = {
                'CURRICULUM': {
                    'Usuario': nomcrip,
                    'DNI': dni,
                    'Titularidad': titulos,
                    'Habilidades': habilidades
                }
            }

            # Create CV complete version
            CVcom = {
                'CURRICULUM COMPLETO': {
                    'Usuario': nomcrip,
                    'Nombre completo': f"{nombre} {apellido1} {apellido2}",
                    'DNI': dni,
                    'Numero seguridad social': ss,
                    'Fecha de nacimiento': fn,
                    'Discapacidad': disc,
                    'Titularidad': titulos,
                    'Habilidades': habilidades
                }
            }

            # Save files
            with open(f"CVs/CVzip/{nomcrip}_{dni}-zip.json", "w") as archivozip:
                json.dump(CVzip, archivozip, indent=4)

            with open(f"CVs/CVcom/{nomcrip}_{dni}-com.json", "w") as archivocom:
                json.dump(CVcom, archivocom, indent=4)

            # Clear fields and show success message
            self.borrar()
            self.show_message("✓ CV guardado exitosamente")

        except Exception as e:
            self.show_message(f"⚠ Error al guardar: {str(e)}", True)

if __name__ == "__main__":
    app = CVForm()
    app.app.mainloop()
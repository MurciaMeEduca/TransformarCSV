import csv

def transformar_csv_a_xml(input_csv, output_xml):
    try:
        # Abrir el archivo CSV
        with open(input_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            registros = []

            # Leer cada fila del CSV y convertirla al formato XML
            for idx, row in enumerate(reader, start=1):
                registro = f"""
    <record id="film_{idx}" model="videoclub.peliculas">
      <field name="name">{row['name']}</field>
      <field name="director" ref="{row['director']}" />
      <field name="actors" eval="[(6,0,[{','.join([f'ref({repr(actor)})' for actor in row['actors'].split('-')])}])]" />
      <field name="release">{row['release']}</field>
      <field name="country">{row['country']}</field>
      <field name="duration">{row['duration']}</field>
      <field name="rating">{row['rating']}</field>
      <field file="{row['file']}" name="cover" type="base64" />
    </record>
                """
                registros.append(registro)

        # Escribir el archivo XML
        with open(output_xml, mode='w', encoding='utf-8') as file:
            file.write('<odoo>\n  <data>\n')
            file.writelines(registros)
            file.write('  </data>\n</odoo>')

        print(f"Archivo XML generado exitosamente: {output_xml}")

    except Exception as e:
        print(f"Error: {e}")

# Cambiar las rutas según tu sistema
input_csv = 'movies.csv'  # Ruta del archivo CSV
output_xml = 'movies.xml'  # Ruta donde se guardará el archivo XML

transformar_csv_a_xml(input_csv, output_xml)

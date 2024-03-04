import xml.etree.ElementTree as ET
import pandas as pd


def convert_to_xml(csv_file, xml_output_file):
    # Step 1: Read the CSV data
    df = pd.read_csv(csv_file, delimiter=";", encoding="iso-8859-1")

    # Step 2, 3, and 4: Process the data and create XML
    root = ET.Element("Articles")

    # Define the mapping between CSV columns and XML elements
    column_to_element_mapping = {
        "Varenummer": "ArticleNumber",
        "Varenavn": "Description",
        "Varegruppe": "Owner",
        "Varegruppenavn": "Usage",
        "Lagerantal": "Quantity",
        "Enhed": "Unit",
        "Stregkode": "Barcode",
        "Vægt": "Weight",
        "Varegruppe": "BillingClass",
        "Leverandørens varenummer": "ExternalArticleNumber",
    }

    for index, row in df.iterrows():
        article_element = ET.SubElement(root, "Article")
        for column_name, element_name in column_to_element_mapping.items():
            ET.SubElement(article_element, element_name).text = str(row[column_name])

    # Step 4: Write the XML to a file
    tree = ET.ElementTree(root)
    tree.write(xml_output_file, encoding="iso-8859-1", xml_declaration=True)

    print(f"XML conversion complete. Output saved to {xml_output_file}")


if __name__ == "__main__":
    # Replace 'your_input_file.csv' with the actual CSV file name and path
    input_csv_file = "./products.csv"
    # Replace 'output.xml' with the desired output XML file name and path
    output_xml_file = "output.xml"

    convert_to_xml(input_csv_file, output_xml_file)

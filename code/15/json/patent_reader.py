import os
from bs4 import BeautifulSoup


def wrtie_json_file(patent_info):
    import json
    with open("output/patent_data.json", "w") as f:
        json.dump(patent_info, f)


patent_dir = "data"
file_list = os.listdir(patent_dir)

patent_info = {}

for patnet_file_name in file_list:
    full_path = patent_dir + "/" + patnet_file_name
    if os.path.isfile(full_path):
        with open(full_path, "r") as patent_document_file:
            patent_contents = "".join(patent_document_file.readlines())

            soup = BeautifulSoup(patent_contents, "xml")

            patnet_documnet = {}
            invetion_title = soup.find("invention-title").get_text()
            patnet_documnet["invention-title"] = invetion_title

            publication_reference_tag = soup.find("publication-reference")
            p_document_id_tag = publication_reference_tag.find("document-id")
            p_country = p_document_id_tag.find("country").get_text()
            p_doc_number = p_document_id_tag.find("doc-number").get_text()
            p_kind = p_document_id_tag.find("kind").get_text()
            p_date = p_document_id_tag.find("date").get_text()

            patnet_documnet["country"] = p_country
            patnet_documnet["doc-number"] = p_doc_number
            patnet_documnet["kind"] = p_kind
            patnet_documnet["date"] = p_date


            application_reference_tag = soup.find("application-reference")
            a_country = p_document_id_tag.find("country").get_text()
            a_document_id_tag = publication_reference_tag.find("document-id")
            a_doc_number = a_document_id_tag.find("doc-number").get_text()
            a_date = a_document_id_tag.find("date").get_text()

            patent_key_value = a_doc_number
            # print(patent_key_value)

            patnet_documnet["application-country"] = a_country
            patnet_documnet["application-date"] = a_date

            patent_info[patent_key_value] =  patnet_documnet

    print(patent_info)

wrtie_json_file(patent_info)
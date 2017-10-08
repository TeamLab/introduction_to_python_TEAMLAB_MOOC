import os
import urllib
import csv
from bs4 import BeautifulSoup


def writeToCSV(patent_infos):
    with open("output/patent_csv.csv", "w") as csv_file:
        cw = csv.writer(csv_file, delimiter=',', quotechar='"')
        for patent_info in patent_infos:
            cw.writerow(patent_info)


patent_dir = "input/patent"
file_list = os.listdir(patent_dir)

patent_infos = []
patent_info = []

for patnet_file_name in file_list:
    full_path = patent_dir + "/" + patnet_file_name
    if os.path.isfile(full_path):
        with open(full_path, "r") as patent_document_file:
            patent_contents = "".join(patent_document_file.readlines())

            print
            patent_contents

            soup = BeautifulSoup(patent_contents, "xml")
            invetion_title = soup.find("invention-title").get_text()

            publication_reference_tag = soup.find("publication-reference")
            p_document_id_tag = publication_reference_tag.find("document-id")
            p_country = p_document_id_tag.find("country").get_text()
            p_doc_number = p_document_id_tag.find("doc-number").get_text()
            p_kind = p_document_id_tag.find("kind").get_text()
            p_date = p_document_id_tag.find("date").get_text()

            application_reference_tag = soup.find("application-reference")
            a_document_id_tag = publication_reference_tag.find("document-id")
            a_country = p_document_id_tag.find("country").get_text()
            a_doc_number = p_document_id_tag.find("doc-number").get_text()
            a_date = p_document_id_tag.find("date").get_text()

            patent_info.append(invetion_title)
            patent_info.append(p_country)
            patent_info.append(p_doc_number)
            patent_info.append(p_kind)
            patent_info.append(p_date)

            patent_info.append(a_country)
            patent_info.append(a_doc_number)
            patent_info.append(a_date)

            patent_infos.append(patent_info)
            patent_info = []

writeToCSV(patent_infos)
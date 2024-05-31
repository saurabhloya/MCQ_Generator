import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        except Exception as e:
            print(e)
            raise Exception("Error reading the PDF file")
    
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        raise Exception("unsupported file format only PDF or text file supported")
    
def get_table_data(quiz_str):
    try:
        quiz_dict=json.loads(quiz_str)
        quiz_table_date=[]

        for k,v in quiz_dict.items():
            mcq=v['mcq']
            options=" || ".join(
                [
                    f"{option}->{option_value}" for option,option_value in v["options"].items()
                ]
            )
            correct=v["correct"]
            quiz_table_date.append({"MCQ":mcq,"Choices":options,"Correct":correct})
        return quiz_table_date
    except Exception as e:
        traceback.print_exception(type(e),e,e.__traceback__)
        return False



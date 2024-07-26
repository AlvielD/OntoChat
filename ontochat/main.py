import ontolib

from ontolib import ChatInterface

from verbaliser import verbalise_ontology
from utils import read_key, read_list
from ontolib import extract_competency_questions, test_competency_questions
from ontolib import split_cq_test_data

from huggingface_hub import login


TOKEN = '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'

def main():

    login(token=TOKEN)

    interface = ChatInterface()

    ontology_path = "data/musicmeta.owl"

    onto_about = "music metadata"
    onto_desc  = "The ontology is supposed to describe music metadata  related to "\
        "artists, compositions, performances, and recordings."
    
    verb = verbalise_ontology(ontology_path, onto_about, onto_desc)

    extracted_cqs = extract_competency_questions(
        onto_verbalisation=verb,
        chat_interface=interface
    )

    cq_list = [
        "Who are the parents of a music artist?",
        "Where did a music artist study?",
        "What is the genre of a music entity?",
        "Who are the authors of a music entity?"
    ]

    cq_dict = test_competency_questions(verb, cq_list, chat_interface=interface)
    print(cq_dict)


if __name__ == '__main__':
    main()
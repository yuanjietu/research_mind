from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import os

def create_sectional_index(index_dir, sections):
    """Creates a Whoosh index based on sections of a research paper."""
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)

    schema = Schema(section=ID(stored=True), content=TEXT)
    ix = create_in(index_dir, schema)
    writer = ix.writer()

    for section_name, content in sections.items():
        writer.add_document(section=section_name, content=content)
    writer.commit()

def retrieve_information(query, index_dir="indexdir"):
    """Retrieves relevant information from the indexed sections."""
    ix = open_dir(index_dir)
    with ix.searcher() as searcher:
        query_parser = QueryParser("content", ix.schema)
        parsed_query = query_parser.parse(query)
        results = searcher.search(parsed_query, limit=5)  # Get top 5 results
        return [result['content'] for result in results]

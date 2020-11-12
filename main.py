import os
from enum import Enum

import panel as pn
import elasticsearch as es
import pandas as pd
import pandasticsearch as pdsh


class PipelineStatus(Enum):
    red = 'failure'
    yellow = 'unstable'
    green = 'success'


def es_data():
    url = os.getenv('ELASTICSEARCH_URL')
    index = 'mb'
    db = es.Elasticsearch(
        url
    )   
    table = db.search(index='mb')
    return table


def dummy_data():
    return pd.DataFrame.from_records(
        data=(
            ('aws', 'failure'),
            ('aws future', 'succes'),
            ('aws next', 'unstable'),
            ('aws ovn next', 'success'),
            ('azure', 'failure'),
            ('gcp', 'failure')
        ),
        columns=['pipeline', 'status']
    )



def main():
    table = es_data()
    mb = pdsh.Select.from_dict(table).to_pandas()
    df0 = dummy_data()

    pn.Column(*(pn.widgets.Button(name=p, button_type=p) 
    for p in pn.widgets.Button.param.button_type.objects))



if __name__ == '__main__':
    main()

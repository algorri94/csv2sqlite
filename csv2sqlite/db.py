from sqlalchemy import create_engine


class CSVDatabase:

    def save_csv(self, file_iterator, table_name):
        processed_records = 0
        chunk = file_iterator.get_chunk()
        print('Inserting {0} record(s). Total processed records are {1}'.format(len(chunk), processed_records))
        chunk.to_sql(table_name, con=self.engine, if_exists='replace', index=False)
        processed_records += len(chunk)
        for chunk in file_iterator:
            print('Inserting {0} record(s). Total processed records are {1}'.format(len(chunk), processed_records))
            chunk.to_sql(table_name, con=self.engine, if_exists='append', index=False)
            processed_records += len(chunk)
        print('Inserted {0} records.'.format(processed_records))

    def __init__(self, conn_str='/db/csv2sqlite.db'):
        self.engine = create_engine('sqlite://'+conn_str)

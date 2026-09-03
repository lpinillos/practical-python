import csv
import logging

log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False) -> list:
    '''
    Parse a CSV file into a list of records
    '''
    if isinstance(lines,str):
            raise RuntimeError("The parameter can't be a string")
    
    rows = csv.reader(lines,delimiter=delimiter)
    records = []
    indices = []

    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    if has_headers:    
        headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

    for rowno, row in enumerate(rows, start=1):
        try:
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types,row)]
            if has_headers:
                record = dict(zip(headers,row))
                records.append(record)
            else:
                record = tuple(row)
                records.append(record)
        except ValueError as e:
            if not silence_errors:
                log.warning("Row %d: Couldn't convert %s",rowno,row)
                log.debug("Row %d: Reason %s",rowno,e)
                
    return records

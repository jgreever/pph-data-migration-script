# PPH Data Migration Script

This script is used to migrate the data from the Salesforce DB that PPH currently uses to the WonderTix DB.

## Usage

1. Enable the virtualenv. If you don't have a virtualenv, create one with `python -m venv venv`
   1. linux/macOS: `source venv/bin/activate`
   2. Windows: `venv\Scripts\activate.bat`
2. Install the requirements: `pip install -r requirements.txt`
3. Edit the file_migration.py file to match any new files that you have created. (This will be updated in more detail later)
4. Run the script: `python file_migration.py`


## Output

All CSV's that you have migrated will go in the `Gold_tables` folder when finished.

The `Silver_tables` folder will contain CSV's that are about ready to be migrated

The `Bronse_tables` folder contains the original CSV files from the Salesforce database export.

To run scripts in order to generate tables, run the scripts in the following order:

file_migration.py
sha_key_hash.py

Chat GPT4 was used to generate faked user data of the PPH database, however, one may also see examples in the Data_Faking folder of the equivalent use of the faker library for the notes table.

These would be could be ran after sha_key_hash.py.


# Scripts
Some light scripts that we have made that handle the registration assigning of WAC

# Usage
1. Get the 2 sets of data and rename them to the filenames that are read in the `FirebaseToCSV` and `GSheetsToCSV` file and put them in the Data folder.
2. Check the `PlenAssign` script to make sure that the variable values (room capacities, plenary lineup etc) are right.
3. Start running the scripts in order `GSheetsToCSV/FirebaseToCSV -> CombineCSV -> PlenAssign`.
4. You should now have a file populated with all of the plenaries for each person.
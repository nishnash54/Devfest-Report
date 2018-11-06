## Data description

#### Devfest2018

 - [X] <b>Source</b>: Gravitas event coordiinator portal
 - [X] <b>File name</b>: devfest.csv
 - [X] <b>Shape</b>: 449 X 7

<b>File</b>: [devfest.csv](./devfest.csv)
<b>Data definition</b>: [devfest_describe.md](./devfest_describe.md)

#### DevTalks2018

 - [X] <b>Source</b>: Gravitas event coordiinator portal
 - [X] <b>File name</b>: devtalks.csv
 - [X] <b>Shape</b>: 1053 X 7

<b>File</b>: [devtalks.csv](./devtalks.csv)
<b>Data definition</b>: [devtalks_describe.md](./devtalks_describe.md)

#### Devfest2018 individual registrations

 - [X] <b>Source</b>: Hackerearth portal
 - [X] <b>File name</b>: devfest-registered.xlsx
 - [X] <b>Shape</b>: 487 X 10

<b>File</b>: [devfest-registered.xlsx](./devfest-registered.xlsx)
<b>Data definition</b>: [registrations_describe.md](./registrations_describe.md)

#### Devfest2018 team registrations

 - [X] <b>Source</b>: hackerearth portal
 - [X] <b>File name</b>: devfest-teams.xlsx
 - [X] <b>Shape</b>: 733 X 12

<b>File</b>: [devfest-teams.xlsx](./devfest-teams.xlsx)
<b>Data definition</b>: [teams_describe.md](./teams_describe.md)

#### Campaign manager

 - [ ] <b>Source</b>: Mlabs MongoDB
 - [X] <b>File name</b>: campaign_data.csv
 - [X] <b>Shape</b>: 265 X 18

<b>File</b>: [campaign_data.csv](./campaign_data.csv)
<b>Data definition</b>: [campaign_describe.md](./campaign_descirbe.md)

<b>Generating updated dataset</b>

Paste the ```credentials.py``` into the dataset folder.
Run the ```mongo_to_csv.py``` script
```py
python mongo_to_csv.py
```
The script will generate the updated ```camapign_data.csv``` file after querying the database.
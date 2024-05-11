# DOJAPI
Requirements:
- Node.js
- Python3
- Flask
- Wekan via Snap


## Deployment

Wekan was installed using Snap and set to continously run on port 5000.
We used AppsScript to trigger the 'sendToWekan' request to the Flask API.

To Initiate the Flask API, we used the command 'python3 wekanapi.py'.
This was made to continuously stay alive on port 5001.

The Apps Script sends the data to the Flask API which is then pushed to Wekan using the Python API parameters to create and add the card to the Wekan board.

Note: Scripts will need to be edited incase the IDs for the parameters of the APIs change. Example: BoardID may change from current boardID to new boardID when domain/ip/server is changed. This could go for UserID, BoardID, SwimlaneID, ListsID, etc...

===================================================

Apps Script needs to be set up within the same Google Account that owns the DOJ Submission form and DOJ: Inbox Spreadsheet.

===================================================

## WeKan Initial Setup

The very first user that is registered on Wekan will become the admin of the board. Current user is DOJAdmin. Once this is done, the import of the json from trello can be imported.

*Very Important*
Accounts such as usernames MUST be set up first in order for the organization of the import to look correct and assign / map the users to each board that exist etc... an email is required for registering each user. I used a generic username@gmail.com set up for this even if the emails don't really work because we did not activate email sending via Wekan. 

Make sure the DOJ: Inbox board is made public or the API will not be able to write to it.

## WeKan Initial Setup

We can use "snap save wekan" to save a current snapshot.
We can then use the following steps to move the existing Wekan board we used for testing over to the new server so we can avoid importing the trello json because this json would need to be converted correctly also, which would include further testing to make sure the import is correct.

Using the snapshot from snap we can already have all users and files already set up ready to go.

'sudo snap ack /path/to/your/snapshot-file.assert'
'sudo snap restore <snapshot-id>'

"Current snapshot id = 2_wekan_6.09_1999.zip"

we can then "snap start wekan"
we can also "snap stop wekan"


## Built With

* [Wekan Installed via snap]([http://www.dropwizard.io/1.0.2/docs/](https://github.com/wekan/wekan-snap/wiki/Install#run-wekan-on-local-network-on-selected-port-on-computer-ip-address)) - The Kanban Style Board
* [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/) - Flask Dependency
* Node.js via NPM
* Python3

## Contributing

Please read [README.md](https://github.com/klrmac) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors
* **klrmac - Dexter Whiz** - *Initial work* - [KLRMAC](https://github.com/klrmac)

## Acknowledgments

* Hat tip to anyone whose code was used namely WeKan Python API and REST API.

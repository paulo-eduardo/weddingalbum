First of all, you have to create an credential in an AWS server and create an s3 bucket named 'albumcasamento' or create a new bucket and configure it in view.py
	to configure an credential you can use this command aws configure

To run backend python app you have to make sure you install this packages:
	django
	boto3
	djangorestframework
	djangorestframework-jwt
	django-cors-headers
One more thing before you can run the server, config a super user that can aprove new pictures

Then you can run python manage.py runserver inside the backend project

To run frondend you just have to run npm install inside of the frontend project folder to install dependences and then run npm run dev

now you can open the site with link http://localhost:8080/

You have 3 pages:
	Public, with pictures that were already aproved and can be liked
	Approve, just superuser can look into this one, it is use to aprove or reject new pictures uploaded for friends
	Upload, as said before, friends can upload pictures from the wedding so you can approve and then finally all your friends can see and like the hole album from your wedding.
	
	
You can also use in this link https://frontweddingalbum.herokuapp.com/#/

For admin page the possibles login are:
	Login: noivo / noiva
	Password: senhaNoivo / senhaNoiva

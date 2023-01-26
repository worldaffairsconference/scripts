package main

import (
	"log"

	firebase "firebase.google.com/go"
	"golang.org/x/net/context"
	"google.golang.org/api/option"
)

func getEmails() {
	// Initialize Firebase app
	opt := option.WithCredentialsFile("key.json")
	config := &firebase.Config{
		DatabaseURL: "https://worldaffairscon-8fdc5-default-rtdb.firebaseio.com",
	}
	ctx := context.Background()
	app, err := firebase.NewApp(ctx, config, opt)
	client, err := app.Auth(ctx)

	log.Fatalln("error initializing app:", err)

	Use(client)

	log.Fatalln("error initializing Auth:", err)

}

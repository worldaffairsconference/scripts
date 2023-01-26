package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"strings"

	firebase "firebase.google.com/go"
	"firebase.google.com/go/auth"
	"github.com/google/uuid"
	"golang.org/x/net/context"
	"google.golang.org/api/option"
)

var accessCode = "THOZYirJHLYj9UXKnypCs9vbeTw1"

func importUCC() {
	// Initialize Firebase app
	opt := option.WithCredentialsFile("key.json")
	config := &firebase.Config{
		DatabaseURL: "https://worldaffairscon-8fdc5-default-rtdb.firebaseio.com",
	}
	ctx := context.Background()
	app, err := firebase.NewApp(ctx, config, opt)

	log.Fatalln("error initializing app:", err)

	client, err := app.Auth(ctx)

	log.Fatalln("error initializing Auth:", err)

	if err != nil {
		log.Fatalln("error initializing app:", err)
	}

	// Get students from csv
	students, err := getStudents("./test.csv")
	if err != nil {
		log.Fatalln("Error getting students from csv:", err)
	}

	// Register students to Firebase auth
	for _, student := range students {
		email := student["email"]
		name := student["pre_first_name"] + " " + student["last_name"]
		grade := strings.Replace(student["grade"], "Year ", "", 1)
		uccAdvisor := student["advisor"]
		studentNum := student["id"]
		temp := uuid.NewString()
		fmt.Println(email, name, grade, uccAdvisor, studentNum, temp)
		params := (&auth.UserToCreate{}).
			Email(email).
			Password(temp).
			Disabled(false)
		u, err := client.CreateUser(ctx, params)
		if err != nil {
			log.Fatalf("error creating user: %v\n", err)
		}
		log.Printf("Successfully created user: %v with email %v, and temporary password %v", u, email, temp)
	}
}

func getStudents(csvPath string) ([]map[string]string, error) {
	file, err := os.Open(csvPath)
	if err != nil {
		return nil, fmt.Errorf("error opening csv file: %v", err)
	}
	defer file.Close()

	reader := csv.NewReader(file)
	records, err := reader.ReadAll()
	if err != nil {
		return nil, fmt.Errorf("error reading csv file: %v", err)
	}

	students := make([]map[string]string, len(records)-1)
	for i, record := range records[1:] {
		student := make(map[string]string)
		for j, field := range record {
			student[records[0][j]] = field
		}
		students[i] = student
	}

	return students, nil
}

func sendPasswordResetEmail(email string) error {

	return nil
}

func Use(vals ...interface{}) {
	for _, val := range vals {
		_ = val
	}
}

# include <LiquidCrystal.h>

LiquidCrystal lcd(2,3,4,5,6,7);
int p;//tank a
int q;// tank b
byte one[] = {
  B10000,
  B10000,
  B10000,
  B10000,
  B10000,
  B10000,
  B10000,
  B10000
};
byte five[] = {
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111
};
byte four[] = {
  B11110,
  B11110,
  B11110,
  B11110,
  B11110,
  B11110,
  B11110,
  B11110};
byte three[] = {
  B11100,
  B11100,
  B11100,
  B11100,
  B11100,
  B11100,
  B11100,
  B11100};
byte two[] = {
  B11000,
  B11000,
  B11000,
  B11000,
  B11000,
  B11000,
  B11000,
  B11000};

unsigned long previousMillis1 = 0;
const long period1 = 1000;
unsigned long previousMillis2 = 0;
const long period2 = 1000;


#include <Servo.h>
Servo servo_1;
Servo servo_2;
const int Relay=A0; // A0 - Relay

int ST1=8; // sonar 1 Trigger
int SR1=9; // sonar 1 Receiver

int ST2=10; // D11 sonar 2 receiver
int SR2=11; // D11 sonar 2 receiver

int Water_sensor=A1; // A1- water sensor

void setup() {
    // for LCD//////////////
    lcd.begin(16,2);
    lcd.createChar(1,one);
    lcd.createChar(5,five);
    lcd.createChar(3,three);
    lcd.createChar(2,two);
    lcd.createChar(4,four);
    //////////////////////////



    servo_1.attach(12); // D12- servo 1
    servo_2.attach(13); // D13- servo 2
    pinMode(Relay,OUTPUT);
    pinMode(ST1,OUTPUT);
    pinMode(ST2,OUTPUT);
    pinMode(SR2,INPUT);
    pinMode(SR1,INPUT);
    
    //LED LAD LID
    pinMode(A4,OUTPUT);
    pinMode(A3,OUTPUT);
    pinMode(A2,OUTPUT);  
    pinMode(A1,INPUT);


    Serial.begin(9600);
 
 
}

void loop() {
    int W=analogRead(Water_sensor);
    //  delay(500);
    //Distance A

    digitalWrite(ST1, LOW);
    delayMicroseconds(2);

    digitalWrite(ST1, HIGH);
    delayMicroseconds(10);
    digitalWrite(ST1, LOW);

    int durationA = pulseIn(SR1, HIGH);
    int distanceA = ((durationA * 0.034 / 2)-4); // Calculate the distance in centimeters

    Serial.print("Distance_A: "); // Print the distance in centimeters
    Serial.print(W);

    Serial.println(" cm");

    //Distance_B
    digitalWrite(ST2, LOW);
    delayMicroseconds(2);
    
    digitalWrite(ST2, HIGH);
    delayMicroseconds(10);
    
    digitalWrite(ST2, LOW);
    
    int durationB = pulseIn(SR2, HIGH);
    int distanceB = ((durationB * 0.034 / 2)-3); // Calculate the distance in centimeters
    
    Serial.print("Distance_B: "); // Print the distance in centimeters
    Serial.print(distanceB);
    Serial.println(" cm");

    unsigned long currentMillis = millis();
    /////very essential to update display
 
    if (currentMillis - previousMillis1 >= period1) {
   	 previousMillis1 = currentMillis;
   	 lcd.clear();

   	 lcd.setCursor(11,0);
   	 lcd.write("tank1");
   	 p=100-(100*distanceA/10);
   	 for(int i=0;i<=p/10;i++){
   			 if (p%10==0){
   				 lcd.setCursor(i,0);
   				 lcd.write(byte(5));
   			 }
   		 else if (p>10&&p%10!=0){
   			 if((p%10==2)||(p%10==1)){
   				 lcd.setCursor(i,0);
   				 lcd.write(byte(5));
   				 lcd.setCursor(i+1,0);
   				 lcd.write(byte(1));
   				 delay(1);
   			 }
   			 else if((p%10==4)||(p%10==3)){
   				 lcd.setCursor(i,0);
   				 lcd.write(byte(5));
   				 lcd.setCursor(i+1,0);
   				 lcd.write(byte(2));
   				 delay(1);
   			 }
   			 else if((p%10==6)||(p%10==5)){
   				 lcd.setCursor(i,0);
   				 lcd.write(byte(5));
   				 lcd.setCursor(i+1,0);
   				 lcd.write(byte(3));
   				 delay(1);}
   		   
   			 else if((p%10==8 )||(p%10==7)){
   				 lcd.setCursor(i,0);
   				 lcd.write(byte(5));
   				 lcd.setCursor(i+1,0);
   				 lcd.write(byte(4));
   				 delay(1);
   			 }
   			 else if((p%10==9)||(p%10==0)){
   				 lcd.setCursor(i,0);

   				 lcd.write(byte(5));
   				 lcd.setCursor(i+1,0);
   				 lcd.write(byte(5));
   				 delay(1);
   			 }
   		 }
   		 
   		 else if(p<10){
   			 if (p==2||p==1){
   				 lcd.setCursor(0,0);
   				 lcd.write(byte(1));
   			 }

   			 else if (p==3||p==4){
   				 lcd.setCursor(0,0);
   				 lcd.write(byte(2));
   			 }

   			 else if (p==5||p==6){
   				 lcd.setCursor(0,0);
   				 lcd.write(byte(3));
   			 }

   			 else if (p==7||p==8){
   				 lcd.setCursor(0,0);
   				 lcd.write(byte(4));
   			 }
   		 }


   		 //////////TANK B///////////////////////////////
   		 ///tank 2 bar code
   		 lcd.setCursor(11,1);
   		 lcd.write("tank2");
   		 q=100-(100*distanceB/10);
   		 
   		 for(int j=0;j<=q/10;j++){
   		 
   			 if (q%10==0){
   				 lcd.setCursor(j,1);
   				 lcd.write(byte(5));
   			 }
   			 
   			 else if (q>10&&q%10!=0){
   				 if((q%10==2)||(q%10==1)){
   					 lcd.setCursor(j,1);
   					 lcd.write(byte(5));
   					 lcd.setCursor(j+1,1);
   					 lcd.write(byte(1));
   					 delay(1);
   				 }
   				 
   				 else if((q%10==4)||(q%10==3)){
   					 lcd.setCursor(j,1);
   					 lcd.write(byte(5));
   					 lcd.setCursor(j+1,1);
   					 lcd.write(byte(2));
   					 delay(1);
   				 }
   				 
   				 else if((q%10==6)||(q%10==5)){
   					 lcd.setCursor(j,1);
   					 lcd.write(byte(5));
   					 lcd.setCursor(j+1,1);
   					 lcd.write(byte(3));
   					 delay(1);
   				 }
   				 
   				 else if((q%10==8 )||(q%10==7)){
   					 lcd.setCursor(j,1);
   					 lcd.write(byte(5));
   					 lcd.setCursor(j+1,1);
   					 lcd.write(byte(4));
   					 delay(1);
   				 }
   				 
   				 else if((q%10==9)||(q%10==0)){
   					 lcd.setCursor(j,1);

   					 lcd.write(byte(5));
   					 lcd.setCursor(j+1,1);
   					 lcd.write(byte(5));
   					 delay(1);
   				 }
   			 }
   			 
   			 else if(q<10){
   				 if (p==2||p==1){
   					 lcd.setCursor(0,0);
   					 lcd.write(byte(1));
   				 }

   				 else if (q==3||q==4){
   					 lcd.setCursor(0,0);
   					 lcd.write(byte(2));
   				 }

   				 else if (q==5||q==6){
   					 lcd.setCursor(0,0);
   					 lcd.write(byte(3));
   				 }

   				 else if (q==7||q==8){
   					 lcd.setCursor(0,0);
   					 lcd.write(byte(4));
   				 }
   			 }
   		 }
   	 }
   		   
   		   
   		   
   	 if (currentMillis - previousMillis2 >= period2) {
   		 previousMillis2 = currentMillis;
   		 if(distanceA<3&&distanceB>7){
   			 servo_1.write(10);
   			 servo_2.write(120);
   			 digitalWrite(Relay,LOW);
   		 }

   		 // for tank a
   		 else if(distanceA>4&&W>300){
   			 servo_1.write(120);
   			 servo_2.write(120);
   			 digitalWrite(Relay,LOW);
   			 delay(5000);
   		 }
   		 
   		 // for tank b
   		 else if(distanceA<3&& W>320&&distanceB>4){
   			 servo_1.write(120);
   			 servo_2.write(20);
   			 digitalWrite(Relay,LOW);
   			 delay(5000);
   		 }
   	 
   		 else{
   		 digitalWrite(Relay,HIGH);
   		 }
   	 }
    }


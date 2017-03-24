// These are the motor pins-- Arduino Shield L298P
const int
dir_a=12,
dir_b=13,
speed_a=3,
speed_b=11,
brake_a=9,
brake_b=8;

char 
move_forward='a',
move_forward_double='b',
move_backward='c'; 

void setup() {
  // put your setup code here, to run once:
  pinMode(dir_a,OUTPUT);
  pinMode(dir_b,OUTPUT);
  pinMode(brake_a,OUTPUT);
  pinMode(brake_b,OUTPUT);

  Serial.begin(57600);
  Serial1.begin(57600); // This is Leonardo

}

void loop() {
  //Serial.println(Serial1.read());
    if (Serial1.available())
    {
         char data= Serial1.read();
           if(data=='a')
           {
        //motor pins here
            Serial.println("got something:::: a");
            digitalWrite(brake_a,LOW);
            digitalWrite(brake_b,LOW);
            digitalWrite(dir_a,HIGH);
            digitalWrite(dir_b,HIGH);
            analogWrite(speed_a,200);
            analogWrite(speed_b,200);
        }
       if (data=='b'){
            Serial.println("got something: b");
            digitalWrite(brake_a,LOW);
            digitalWrite(brake_b,LOW);
            digitalWrite(dir_a,HIGH);
            digitalWrite(dir_b,HIGH);
            analogWrite(speed_a,0);
            analogWrite(speed_b,0);

        }

       if (data == 'c'){
        
            Serial.println("there something here a C");
            digitalWrite(brake_a,LOW);
            digitalWrite(brake_b,LOW);
            digitalWrite(dir_a,LOW);
            digitalWrite(dir_b,LOW);
            analogWrite(speed_a,255);
            analogWrite(speed_b,255);
        }

   
}
}

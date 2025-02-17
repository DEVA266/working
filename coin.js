let guess = " ";
function flip(){
  const randomnumber = Math.random();
  let answer = " ";
  if ( randomnumber <= 0.5){
    answer = "HEAD";
  }
  else {
    answer = "TAIL";
  }
  console.log(answer);
  let result = " ";
  if (guess === answer){
    result = "your guess is right"
    alert(`The Flip Output is ${answer} and you guess ${guess},${result}`);
  }
  else {
    result = "yor guess is wrong , you loss the game";
    alert(`The Flip Output is ${answer} and you guess ${guess},${result}`);
  }
}


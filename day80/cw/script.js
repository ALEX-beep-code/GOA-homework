const myfunc = (Text) => Text.length
console.log(myfunc("hi"))

const price = function(price , sale){
    return price * sale / 100
}

const df = (number) => {
    if (number%2 == 0){
        return "ლუწია"
    }
    else{
        return "კენტია"
    }
}

const con = (score) => {
    if(score > 90){
        return "excellent"
    }
    else if(score > 70){
        return "good"
    }
    else if(score > 50){
        return "passed"
    }
    else{
        return "failed"
    }
}

let score = 60
const check = (score < 50) ? "failed" : "passed"

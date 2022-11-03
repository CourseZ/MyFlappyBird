my_func <- function(sotien) {
    to_500 <- as.integer(sotien/500)
    sotien <- sotien - to_500*500
    to_200 <- as.integer(sotien/200)
    sotien <- sotien - to_200*200
    to_100 <- as.integer(sotien/100)
    sotien <- sotien - to_100*100
    to_50  <- as.integer(sotien/50)
    sotien <- sotien - to_50*50
    to_20  <- as.integer(sotien/20)
    sotien <- sotien - to_20*20
    to_10  <- as.integer(sotien/10)
    sodu <- sotien - to_10*10
message(as.character(to_500), " to 500")
message(as.character(to_200), " to 200")
message(as.character(to_100), " to 100")
message(as.character(to_50), " to 50")
message(as.character(to_20), " to 20")
message(as.character(to_10), " to 10")
message("So du ", as.character(sodu))
}

my_func(1330)
#!eui
-- test program for euphoria cgi
-- comment/uncomment the following to test the EUINC variable

with batch

include std/io.e
include std/pretty.e
include std/get.e
sequence cmd

-- if val is a string, return it, otherwise "Undefined"
function test_val(object val)
    if atom(val) then
        return "Undefined"
    elsif object(val) then
        for i = 1 to length(val) do
            if not atom(val[i]) then
                return "Invalid string sequence"
            end if
        end for
        return val
    else
        return "Invalid type for string"
    end if
    return "foozle" -- never reached
end function


procedure env_dump(sequence val)
     printf(1, "%s: %s\n", {val, test_val(getenv(val))} )
end procedure

puts(1, "Content-Type: text/plain\n\n")
puts(1, "Hello!\n\n")
puts(1, "COMMAND LINE\n============\n\n")

cmd = command_line()
for i = 1 to length(cmd) do
    printf(1, "%d: %s\n", {i, cmd[i]} )
end for

puts(1, "\n\nREMOTE INFO\n===========\n")

env_dump("REMOTE_IDENT")
env_dump("REMOTE_USER")
env_dump("REMOTE_HOST")
env_dump("REMOTE_ADDR")

puts(1, "\n\nSERVER INFO\n===========\n")
env_dump("SERVER_SOFTWARE")
env_dump("SERVER_NAME")
env_dump("GATEWAY_INTERFACE")
env_dump("SERVER_PROTOCOL")
env_dump("SERVER_PORT")
env_dump("REQUEST_METHOD")
env_dump("PATH_INFO")
env_dump("PATH_TRANSLATED")
env_dump("SCRIPT_NAME")
env_dump("QUERY_STRING")
env_dump("AUTH_TYPE")
env_dump("CONTENT_TYPE")
env_dump("CONTENT_LENGTH")
	
puts(1, "\n\nBROWSER INFO\n============\n")
env_dump("HTTP_ACCEPT")
env_dump("HTTP_USER_AGENT")

flush(1)

puts(1, "\n\nSTANDAR INPUT\n=============\n")

object content_size
sequence std_input = {}
object char

content_size = getenv("CONTENT_LENGTH")
puts(1, "Content_size: ")
print(1, content_size)
if atom(content_size) then  -- content length no definido
	puts(1, "\nNo standar input\n\n")
	abort(0)
elsif sequence(content_size) then
	object j = value(content_size)
	puts(1, "\nj= ")? j
	if j[1] = 0 then --value() => GET_SUCESS
		puts(1, "CONTENT_LENGTH: ")
		? j[2]
		for i=1 to j[2] do
			char = getc(0)
			std_input = append(std_input, char)
			puts(1, char)
		end for
		puts(1,"\n\n")
		print(1, std_input)
		--puts(1, "\n")

	end if
else  -- Unexpected error
	puts(1, "There is something strange about CONTENT_LENGTH\n\n")
	abort(0)
end if

/*
for i= 1 to content_size do
	std_input = std_input & getc(0)
end for
*/

print(1, std_input)
--puts(1, "\n")

printf(1, "Entrada estandar recibida tiene %d bytes", {content_size})
-- should match DIR size of "temp"

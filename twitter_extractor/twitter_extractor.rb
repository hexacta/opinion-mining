require 'twitter'

client = Twitter::REST::Client.new do |config|
  config.consumer_key    = "Bl54GPEbaWc0PK8IE0hDqKoL1"
  config.consumer_secret = "XFgd3NrpI3WabmG1weBnrJtfII1vzPoli0RZzxkqnt94uWBGtw"
  config.access_token        = "903872095-1vgP4LFouZ05WWBbHQTlrxf9QpdeiJ55HYFuwepw"
  config.access_token_secret = "bltLHrH8m7ZuWlLfzDc3973CYJm7ucXzBJQxm1yoYSFd4"
end

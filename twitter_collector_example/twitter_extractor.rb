require 'twitter'

client = Twitter::REST::Client.new do |config|
  config.consumer_key    = "Bl54GPEbaWc0PK8IE0hDqKoL1"
  config.consumer_secret = "XFgd3NrpI3WabmG1weBnrJtfII1vzPoli0RZzxkqnt94uWBGtw"
  config.access_token        = "903872095-1vgP4LFouZ05WWBbHQTlrxf9QpdeiJ55HYFuwepw"
  config.access_token_secret = "bltLHrH8m7ZuWlLfzDc3973CYJm7ucXzBJQxm1yoYSFd4"
end

def collect_with_max_id(collection=[], max_id=nil, &block)
  response = yield(max_id)
  collection += response
  response.empty? ? collection.flatten : collect_with_max_id(collection, response.last.id - 1, &block)
end

def printable_tweet(tweet)
  "#{tweet.created_at}    @#{tweet.user.screen_name}    #{tweet.user.name}    #{tweet.text}"
end

def client.get_all_tweets(user)
  collect_with_max_id do |max_id|
    options = {:count => 200, :include_rts => true}
    options[:max_id] = max_id unless max_id.nil?
    user_timeline(user, options)
  end
end

def client.get_home_tweets
  collect_with_max_id do |max_id|
    options = {:count => 200, :include_rts => true}
    options[:max_id] = max_id unless max_id.nil?
    home_timeline(options)
  end
end

OUTPUT_FILE = "output.txt"

# Get Hexacta tweets
tweets = client.get_all_tweets("hexacta").reverse

# Get @agpelliza home timeline tweets
my_tweets = client.get_home_tweets.reverse
File.open(OUTPUT_FILE, "w+") do |f|
  (tweets + my_tweets).each do |tweet|
    puts printable_tweet(tweet)
    f.puts(printable_tweet(tweet))
  end
end

puts "Hexacta: #{tweets.count} tweets"
puts "@agpelliza: #{my_tweets.count} tweets"
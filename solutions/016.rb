# https://leetcode.com/problems/encode-and-decode-tinyurl/

@bank_url = Hash.new

def encode(long_url)
  char_pool = ('a'..'z').to_a + ('A'..'Z').to_a + ('0'..'9').to_a
  base_url = 'https://tinyurl.com/'
  sub_url = String.new
  6.times { sub_url << char_pool.sample }
  complete_url = base_url + sub_url
  @bank_url[complete_url] = long_url
  complete_url
end

def decode(short_url)
  @bank_url[short_url]
end
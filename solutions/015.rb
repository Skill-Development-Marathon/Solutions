# https://leetcode.com/problems/defanging-an-ip-address/

def defang_i_paddr(uuu)
  uuu.gsub(/\./, '[.]')
end
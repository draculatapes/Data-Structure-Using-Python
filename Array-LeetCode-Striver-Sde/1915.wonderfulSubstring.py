#Brute Force

class Solution:
    def isWonderful(self,word):
        letter_count=dict()
        for letter in word:
            if letter in letter_count:
                letter_count[letter]+=1
            else:
                letter_count[letter]=1
        odd_count=0
        for count in letter_count.values():
            if(count%2!=0 and odd_count>0):
                return False
            elif(count%2!=0):
                odd_count+=1
        return True                    
    def wonderfulSubstrings(self, word) -> int:
        count=0
        for i in range(len(word)):
            curr_substring=""
            for j in range(i,len(word)):
                curr_substring+=word[j]
                if(self.isWonderful(curr_substring)):
                    count+=1
        return count            
def main():
    word="ghffghcdigdgbfhaiejibbcidgfjahegedjecfhdjchdcaefeefiabebefjccdhdchacehfdjibcgcedjhhbadfgejhceghgjjegihhbfagciecdadhcjgdajgbhegjhicbifeefcaficcbcijciegihidacjahahjgdjdgfjcadgaiicgiiegaeifjbcjacefffgdgibjfijiiedcaahbceebheifbgffchdcfbbhfdfajggfhhhbhhgbcgfdgcfcdggihhcfcghbgbchcgaccccaabeejdhdbjicghddaaeedciigeeiehjhhhicajbddedidecjiebbggdehbgejabcbcjadicjgbabehbjjbehfegicabighbcahijjdcgehjhcbfheecgjdfbhadgbhfdefffbcbggifgdhdgahgejeegbadbifjdiaggdcjfaiigdjjehebjdabgdecfcebcfggceihffhjcjfaadhgeahiajjdghehieiidcfdjaeiehcjghjcajhgdhcfjcagiibhdiiabghcffaijehjjjiafjcgfjeghdbggbhfjdihahjedgdhhdibcdgaaafejgbdjgdfichbijjajicdfehafjbgdbieaecagdifeggbefegeajejbcfaidjbgbbgejjebidcdaeggcefjdfacachfeehajfabfhbcdjbcjdifiehdjghdhegfgababaeacdjcegffgdhadjehiebggdiececeiihfghcecahbhgefhihahhfhgdeaejgdhihcgfecgecebdjgcjicjdbcicigdbaehhjcdajbehdeahbibeejddajiacgchbcffagbbdiechcfgafehifibifhaidaeidjbeefefcaiejdhibebghbjgbbhchfjeefdfgjiijbbbgchgjhaefdgejfgeegbajgbcjejahgchfhjbgiiggjiaigiibccidcjcgbabed"
    print(word[0:3])
    s1=Solution()
    print(s1.wonderfulSubstrings(word))

main()                
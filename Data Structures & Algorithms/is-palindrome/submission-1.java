class Solution {
    public boolean isPalindrome(String s) {
        String ss = s.replaceAll("[^a-zA-Z0-9]", "");

        int i = 0;
        int j = ss.length() - 1;

        while (i != ss.length()/2) {
            if (Character.toLowerCase(ss.charAt(i)) == Character.toLowerCase(ss.charAt(j))) {
                i++;
                j--;
            }
            else {
                return false;
            }
        }
        return true;
    }
}

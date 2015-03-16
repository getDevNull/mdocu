% A whimsical paper about nothing
% Jack-Benny Persson
% 2015-02-16

# Lorem Ipsum #
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis 
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum.

## A subheading ##
Yes yes, this is indeed a subheading for Lorem Ipsum above. Below is also a
small piece of C code.
```
main()
{
    int net;
    double hosts;
    double addr;
    printf("Enter netmask in slash-notation without the slash: ");
    scanf("%d", &net);

    if (net >= 0 && net <= 32) // Sanity check the user input
    {
        printf("Netmask bit: %d\n\n", net);	
        addr = pow(2, 32-net); // Calculate number of addresses
        printf("%.0lf total addresses\n", addr);

        hosts = addr-2; 
        if (hosts < 0)   // Check if number of usable hosts is a negative value
        {
            hosts = 0;   // Set usable hosts to zero if it was negative
        }   
        printf("%.0lf usable addresses for hosts\n", hosts);
        return 0;
    }
    else  // If the user entered anything else than 0-32
    {
        printf("Only values between 0-32 are accepted\n");
        return 1;
    }

    return 1;
}
``` 

Inline `code examples` can be used like this.

## Some other markdown examples ##
*This is italic text* and this other **text is bold**.
We can also insert som hyperlinks like this. 
[Google](http://www.google.com). Tables are also really easy to make like below.

Command     Explanation 
--------    ----------
ldapadd     Add data to LDAP
ldapdelete  Remove data from LDAP
slaptest    Test slapd.conf

Table: A few OpenLDAP commands

### Boom ###
And Boyle says boom [se @doe99]. Here we saw an example of a reference. At the
very end of our document we specify all of our references we use in this really
nice looking advanced paper on quantum ph...er.. nothing. Of course it is also
possible to include images as shown below.

![Siberian cat (Image by Phattums on Wikimedia)](./Siberian_Forest_Cat.jpg)

# References

---
references:
- id: doe99
  title: Science for us
  author:
  - family: John
    given: Doe
  container-title: Test Materials
  volume: 11
  issue: 4
  publisher: My Own Publishing Group
  page: 261-266
  type: article-journal
  issued:
  -  year: 2012
     month: 3
---

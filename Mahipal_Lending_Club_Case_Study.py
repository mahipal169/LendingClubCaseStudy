#!/usr/bin/env python
# coding: utf-8

# ![Lending_Club_Case_study.jpg](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAeAB4AAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMFBwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz/2wBDAQICAgMDAwYDAwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAz/wAARCACAAV8DASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD8x6K5F/jr4UjYq2qjIOD/AKPN/wDEU5Pjh4WdSw1UED/p3m/+Ir9b/tLC/wDPyP3r/M/Jf7Mxf/PuX3P/ACOsorlB8cPC5OP7VGQM/wDHvN0xn+7SH43+F1d1OqANGdrA28wIP020f2lhf+fkfvX+Yv7Mxf8Az7l9z/yOsorkv+F5+Fhndq3T/p3m/wDiKb/wvXwr/wBBdf8AwHm/+Io/tLC/8/I/ev8AMf8AZmL/AOfcvuf+R19Fcg3x28Jjrq6/+A0v/wARR/wvfwp/0Fh/4Dy//EULMsJ/z8j96/zD+zMX/wA+pfc/8jr6K5Ffjt4UY4/tcH/t3m/+IrqbK8i1GzhuYXEkM6LJG2CNysMg4PI4PetqOKo1W1TmpW7NP8jGthK1JJ1YON+6a/Mlooorc5wooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA+R5v9dL1zuP866D4UfDHxH8aPHem+F/Cujah4g17VpTHa2FlGZJZdoLO2OAFRFZ2ZiFREZmIVSRz20i4kPXcx/nX2P8A8Ej/ANkj4heMP2yPhJ4msvBN/rPhuXVFv5nHluJ7COeKC6dId/myiP7TAZNilo450cja6Ofxc/aD0n9nL/gjz4ntfHt9rOgCy+JD/Dj7TB400vU/D7R2Wl+dAltbXUPmPJ9pjFzLc5W5jt2gbTZmuIFRJFX6S/bf/wCCS8Ov6po3w/0Twv8AD3w/Dr1uNT0bxQ+mTaY+gWcV15uph3a8bzbex0/97/pXyvHD+4QzSM1fst+y18JbX4W6BNprXmh6rbaKz2Vla2Oko0cEMUmoySW0EKQ+YdtteW8W0sCTGQFQAqzdZ0rwd4Y/ZV+I2jeKrLw80t/a+ILXWLJokeKVRZ3D3Q8qNlkdZIVnfAKPskOcbyWAP5Z/2oP+CdmpfBn4Yaj4u0VNa1Twzocscd1qUywyFo5JFjiluYLdpH0tnd0VILxtzMZ49/nW08SfMHlc7cnH61+3v7eXwx0TWv2efF2q+EbiLxDJDpOv363N3bM+tHzdJmlvI5zMNptI7eASYJeT7XbyTYV1SUfk38Vf2Jfih8DPAuleIvG3hS78H2etI01hZa5dW2navd26hj9pTT5pFvGtyFOJvJ8pjwHNAHk0i9GpjSYwB2qRlzk88VGVyRnqKAHupyDnoK+pvA//ACJWj/8AXjB/6LWvlkj92B/dr6m8D/8AIlaP/wBeMH/ota+u4T/jT9F+Z8nxY/3MPV/kalFFFfdHwYUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAfMXw48OWHi74k6BpGrarHoemarqkFne6lJgpp0MkypJOckDCKWbkj7vWv3y/Yy1WK38WeD77xdqeoxWej20Wg3ba9Y22k3X2O2t5tGjM9u10rQm2cQrMZQx4mlLslvI0/8+ZOyWU9w5x+dfqp4T/4KMeD/FX7L+lRPbaPq1va6VaXmvacdTFtr2hXsdndxTQafCybZ7VzpQu0aJHTThqxhYsohEf4uftB+q6/tieCfgh8U2vL74v+DtE07UNNs9T1W41bxLbW76oUjUJfqUKRySz3H2pPLVdskJtwqRqkDJ84/Er/AIKZ+Afi/wCDfiVpHgv4jaFc+K/GHi3UNV8O6ZpWo3V1qE0JmsZ5JllitwsZFrDcBopQsYjkkw9wFZY/x2/bE/4KI/En9om71LwxN4x1C4+H8SW9ha6Snlrb+RbJEI4iw3M8aSxB1UyOm4BlAwDXgnh3xNL4R162v4rayvPszFvIu4vMibcpVuhDKSD95GV1IDKysqsAD9udA+KeneNNG0j4269fxa5pXwygN5qmh2V9ara+MdU8y3fRrW8vIpZGhglnsN8s14PLljmxGkkSzyW3x1+2lrGseJPGPjz4q+KPiH4T8T3fj/TZpr7TLfSb1YJrw2iWrWkSLC8Ea2yTboC8jAeRE+7BE1eJ/D340an+0p4StfD11p6XWtaddNBpVrBci2stOgaazWztYlcYWJpZNQMzzSnzprxJJHaeQtP3P7R/xck+Dnhm+l1p/FWifFbV/DcWjaHbWd1bfYrbR7qxazvWvIXR5EiuLS4uBbx5Ek8d6l1uijS2kvQD4nMWGUDJyM0x4yMnnnmr4sWCl+gUVWnGWI9KEBHDGXOCTk19ReCFP/CGaOOSTZQgcdf3a18vxAqVPQZr9Av+Ca/7Hmoft5fG3wZ8L9L1uz8O3uuaXJMl/dWrXMUQgtGmKlFZSd23HXjOfavquGKsac6lSbskr/ifLcUUpVIU4RV22eY45I64or6x/wCCov8AwSc17/gl3/wgqa74z0jxa/jk6gYVsdPktBa/ZPsuc73bdu+08YxjZ3zx8nV9zh8TTr01UpO6fU+GxFCdGo6dRWa6BRRR645x19q1MW11CijsD60HPJPagLLuFFJztzn5fXFL2BzweR7j1p+YBRRnPfNJkHvR6A33AnBwTz6Hg0uO/P5fh/Ovtj/gmZ/wRO8Tf8FMvgrr/jXQ/HmieFLXQPEEugSWt7psty8zpa21x5gKOoAxchcY6qT3r5+1P9lO9079pL4h/Dc6zbPd/D3Wb/R5777KwjvWtLt7UyJGGyoYx7wCWwDjnrXk4zO8HhoTnVmkoay8ldHu5Vw3j8xxFPCYOm5TqO0V3e/5JnlAbPGcnpxyaK6f4t/DKb4TeKk0i4vYb52t1uBJGhRcMzKFwSe6n9K5jB46nPSuvA42jjKMcRQleEldPujlzfKcTluLngcZDlqQdpLs1ugoo57ZbPPAzRXW33PMk10Cig8euD7cGjsT6UeYaXsFHoM5J445P0o7ZySD0OM55x/OvoT9gr/gmF8Wv+Ci+v3cPgHSrW28P6XMLfUvEerStb6VZybQ3k7lVmmm2FW8uJWI3oXKBlJyr16dKDqVJWXmbUaM6s/Z043fkfPfQ45z19/rSAg5HJx1xziv2O0r/g0jvW0RTf8Ax7t49RdQzLb+DWeCNs5IBa+DMM8ZwvHavk7/AIKDf8EGfjD+wb4PvfF6XGm/ETwHpq773VtHhkhudLj7y3NoxYpF6vG8ioAS5VRmvNo53gqs+SM9fPS531smxdODnOOi7anxHnP8X9O3/wBejOP4v69v/rV9Af8ABNn/AIJ/at/wUm/aA1L4f6L4l0/wtd6boFx4ga8vbWS5jdYbi1gaMIjKQxN0DuzwEI7ij/gpP/wT71f/AIJs/H/TPh/rXiXT/Fd3qfh+38QreWVq9tGiS3N1AsZR2YlgbVm3Z5DAdq61jqPtvq9/etexyfU6vsfbte73Pn+ijB44PNGPfn9a6/M5bruHqeuOPx9KTd15PHHsD6V6J+yN+zvd/tbftL+DPhnY6rbaLeeML82Md/cQmeO0PlPJuKBlLD93jAYda+gv+Cnv/BHTxF/wTD8G+ENZ1vxxo3ixfFmoT6fFFY6dLatbGOISbiXdtwIyMADHHNctTG0YVY0JStKWyOqGDqzpSrRjeK6nx1RRj6kD2NFdfqcqfYKKKKQBRRRQB8ieV/pMp54c/wAzUuNzAHJ4pH4lc55Lt/OnxEmUH1B/lX4uftA5X34UnaBxTXcnJPJNIULE+pNSQIHUk888UAa3w/8AH+v/AAv8U2eveGNb1nw5rumsz2uo6Vey2d5bFkZG2SxsrruRmU4IyrEdDXe/slfsyeLv22/2k/Cvw18KR2tz4m8a6kLaKW9uhbwQ/K0ks80jZIVI0kkbAZ2CEKruQp8vRvJVifwruvhF8etb+DGjeLbLRTYwnxnpDaJeXjWqG/tLZ5Y3lFrcbTJA0saPbybfleK4kVlb5cAH6U/GT4mfsb/8EoDP4H+Bfhax/aN+P1jefY9T8c/EOwa48KeHriGTy7lLewwscvlS2xljmRXEYnD/AG64VHhP5c/FLxqPiL8RtZ8QG0sLFtZu3ungsrX7Jbqznc5SHcwiDOWbYp2KWIUBcAd14/8A2rL/AFPwkfCXg3SLbwL4PjuJplggdbrWLzzYnhl+06kUWZklgMcUlvCILSQQRMbbzFLnykoG5PagBzFmBHrX66f8G0Ax/wAFN/hQOpGhaj/6bJK/IdXyGIJ3Hj8K/Xf/AINoP+Um3wm/7AOo/wDpskr3cof7jEf4Twc6f72h/iR9l/8AB3KMXv7PfqB4j/8AcXX42V+yn/B3Of8ATP2ewOSV8R/+4qvxq3exr7Dhz/cIL1/NnxvEH+/1Pl+SNn4f/D7Xfix450nwx4Y0m/17xDrtytnp+n2URknupW6Ko9gCSThVAJJABI/Tn4Pf8GpnxP8AGHhC3vvGnxO8J+CtWnTf/ZtnpUutNb5AISSXzoEDjoQm9Qfusw5rt/8Ag1J/Zj0zWdR+Jnxg1C2hudS0iaHwrozuuTZ7oxcXbjsGdXtVDDBCiQdHIr0j/gp/+yN+3f8AtVftSaxffDzxRc+EfhrpLLbeHrLR/G0miSTIqLvubgQFWkleTeRvJ2JsACncW8/Mc3qyxTw1Kago7tnpYDKqawyr1YOblsl2Pzy/4KI/8ER/i7/wTt8Nt4q1N9L8a+ABMsU2v6MsinTmdlVPtlu43Qh3YKrq0kecKzKzIrcv/wAE1/8Aglp4y/4Kc6p40tfCHiPwz4efwRFYzXR1YTn7QLs3ATy/KRuhtWzuxjcuM84/f39hr4U/Fjxd+w9P8P8A9qCy0nxB4imiu9Cv5FvI7xNf0ySMKj3DIAPMKO8TcZbyw5yzE18Mf8GzXwpl+An7VH7XHgSaeS6k8F6ppmhGZ12tcC1vNZhEpHq4QN/wKuennlZ4aqrpzhbVbNXsbTyOisTTdmozvo907X3Pmv4T/wDBsr8avH/xr8W+HNX8ReGPDXhrwncw2g8TSW09xHrcslrDck2VudjyRxecI3kd0XzFdVLlX2Yv7fX/AAbufFP9iv4Sal490XxLpXxN8LaBA11rRstPk07UNOgUZe5+zmSUSQoAS7LLuVfmKbVZl9l/4L1f8FbPjH8L/wBt/VPhZ8OPGGqeBdA8B2tkbx9MWNLnVL24t0ujI8pUuI1iniQRggFg5bdldv6K/wDBHb9pbxL+3B/wTe8JeKviHJaazr999v0jVLg26JHqq29zNbiWSNQEDPGqlwoCli2FUEAZ1cxzGjSp4uo1yytp6/5mlLAYCrOeFpp80b6+n+R/NX8Evgl4q/aN+Kei+CPBGjXXiDxR4in+z2Nlb4DOQCzszMQqIihmZ2IVVUkkAV+nHhj/AINPPiHqHgiK71n4weEtJ8QvEJH0220S4vbWOTH3ftRmjYgYHzeR+Fel/wDBrd+y9o/hrX/jh49MYutQ0XW/+EG0ueQZktraEiefB9ZS1ru/64jpmvnL/gtp/wAFXfjBrn7efjDwZ4K+IPivwP4P+HF2NHtLbw9qU2mvd3UaKbi4uJIiryHzmZArExhIlIUMzM3dWzDFYnFvD4VqKirts5KWAw2GwqxGJTk5PRI/SL/ggb+xh4+/YO/Z4+J3gL4iadBZ6tF4/nvLS5tJjPY6ravpemqlzbyFVZoy6SL8yqwaNgVBGK/Lb4Ufsb+P/wBtb/grb+054b+HviHw34c1TS/FviXUbq41qGSaGWEa7JHsUIrHdudTzjhetfq5/wAEF/24vFP7cv7DT6r44u21LxZ4M1yfw3faiyLG+qBIYLiGdlXC7/KuURiANzRs2Oa+SP8AgiXj/h+9+14SOuo+Jf8A1JBXzlSDn9ZjiYqTa1TWj1XQ+kwuMnhauFrYGbhKLvFp6rR9T4o/ag/4Jo/ErQf+Cj3gr4D+JPFXhLUPGfjbT7WSz1S0jnj063ike72LICnmEqbeTOAc7l/D0r4j/wDBs/8AHvwX4/8ACPh7S9X8F+JpPFMlwbnULZ7m3stBhhWMtPcvJHkqzSKqpGHdj0XaGZfp79vXn/g6B/Z/99F0z/0PV6+hv+Dg39vXxz+w3+yv4eHw8v00XxN451s6WNWEKTSadapBJLK0SuColYiNAzKwVWcjDbSPQoYvEUY4fC4RKKcdFbRb/gcGOp08ZWxGOx8nOfNrJu7e258S/EH/AINQviPoXgSW+8OfFjwl4j1+KLzBpV1os2mwzMBkolz5spz1A3RqCcbioyR+XPxA8Eax8KPGOseHvEum3eia54fupbLUrK6XZLZzRttdG7cEdQSpGCCQQT+0v/Bt1/wUb+LH7TnxU8f/AA9+JHivUfGlnp2kR65pt7qOx7uyYTiKWLzAoaRG81CA+dpjOMBsVQ/ah/ZX8P8Axi/4OhfAVheafBLp1x4fsvGWsxlci8uLKG6SFnHQjfa2SsDwyptIIIrvw2a4nD16lHFNS5Yt3R5eJyzDYijTrYZNXkk0fPn7I/8AwbIfFv4//DSx8UeNfFWkfCiPV4FubPSrvSpNS1RY2GVNzCssKQMwIOwuzqDh1RgVFbxh/wAGxvxx8PfHTS/C9j4i8Iar4Z1e3nlt/FWyeO3tJIlDCC5twHkieQbijKzxkIQXViqt9mf8HKv7f/jz9ljwF8PfAXw81/UfCeoeO3vb3VdW02UwX8Vpa+SiQRSr88XmST7i8ZVwIQAwDMDwf/Btl/wUu+I3x8+Jvi34P/EXxNrHjM2WinxJoeqarM1zfWqRTwwXNvJcMTJMrG5gdN+WXbKN2CoXm+vZk8O8cmuV3svLudP1LL1iFg5J8ytr59j8/f2lf+CRXjz9mX9tT4a/A3VNe0DWfEPxO+yG0vtLjmeCyjuLt7ZpJFlVWPliN5SAfuqe9fuf+1T8ZfBX/BE//gmyJ/Cug2psfCltBofhrSGfZ/aWoTMdrTOMF2ZvNuJn++4WVuWNfOX7cAtT/wAHK/7KouypiXwtdlQ3IEhh1nZ+O/bj3qh/wdgi6b9jj4ZbPMNgvjtPNIHy+b/Zt95ef+A+bj8a5qteeNqYenXekld/e/8AI3pUIYOniKtFaxdl9y/zPy48b/8ABZD9qDx746k8QXHxn8X6ddNM0sdppUqWOnwAniNbZF8tkUcDzA5IA3MxyT+qn/BNL/gv78O/it+y8+n/ALR3jXw7oHj3TLmXTbt7mxdYfENoY0KXbRRRmJWYO0bqAFLRkhVVwo/BP0Hc0bccdeccDP4d8f59q+oxWSYWtBQS5WuqWp83hs5xNGbk3zX3Teh+tP8AwQf8P+B/DH/BcT4x2Pwy1W21n4ex+EdXl8PXVusixfYpNT0mRIV3gNti3+TkjJ8r8azv+Dhv4L6h+0h/wWZ+FHw+0q7srDU/GPgvR9Itbm7DGCGSbVtWUO+0FtoPoDXF/wDBrCwH/BSPxNgj/knGo9Ov/IT0mvfv+CqYI/4OSv2YwcHOl+HP/Tzq1fO13KjmTcXrGL19InvUkquXpSWkpLRdmz4Z/wCCjn/BGvx5/wAE0fhr4f8AE/i3xX4Q8QWfiPVv7Ihh0lbgSxSeRJNvbzUUFcRMOD1I46kcL/wTn/4JzeKv+ClHxT17wj4S13QNAvPD+kjVpptWExiljMyxbF8pWO7Mg644HWv1X/4Oxmz+yZ8LBjOfGpyf+4dd183/APBqKR/w2j8SSTwPBa/+l0FejSzKvLK5Ylv3l5eaRw1ctoRzKOHS91/5Hnv7MP7C/iT/AIJ3f8FzPgb8PPFOsaJrupy3MOsC50zzfs4jmgvUCYkVTuBibt0I564/R7/gvR+wV8Qf+ChWn/Bzwd4BtLHzLPW7291TUtQlMNhpNv8AZ1TzZWALMS7BVjRWZ2PTarsvg37cIz/wdD/AfIxnSNOP/juq19B/8HDP7ePjD9in9k7QbP4f6rLoXivx/rJ01dUiRWuNPs4oXluHh3AhZWIijDkHasrspVwrDx8RXr1sRh5xtzuKt+Op62HoUaOHrwnpCMv8j4p+JX/BqJ8R/Dvgma98K/Fjwl4p12BDIul3mjTaVFMRg+WlwJpvmPON6KCcZKjJH5gfEf4b6/8ACDx/rPhXxVpF9oPiTw/dNZajp93HtmtZVPKnGQQQQwdSVZWVlJVgT+mH/BAL/gqV8V9T/bj0P4XePPHPijx14Y+IUF3Bb/2/fyahcaZewW0l0kkc0paQIywSxmPdtJdCACvO7/wdc/s/6Z4V+M/wt+JNhbxQaj4s0+80XVmUbfPazaGS3c4+8+y4mQsedscYPAGPaweOxNHGfVMU1LmV00eRjMHh62D+t4ZcvK9UfkxRRRX0x80FFFFAHyXLH5buOTlyf1oik2sTjJxSyqZpJB6sf50RBhIpPQcZ7V+Ln7QDhiM/3qlij+RWyeKaDibPXdVi1IL8nINACSKGKgjtSi2IhbDZ4zk9qn2j7ODgkk8fnSRxP5LAAnOc/lQBFb2+YlLfeGf5UKhAZsZAGPxrq/gV8M7j4z/GXwj4Ntppre78W63ZaNFJDZveyxvcTpCGWBPnmYF+I15c4Ucmv3G/Zt/4Ji/ED45eBbbU/gF4H8Ofs6+BbmzVbnX7yGf/AISnT5orsfa7ddSdBqNzJlFdgrizBh8uNo3QtQB+A6SqZxjp0Nfrx/wbS/8AKTf4Uk5AOhaj/wCmyT+lfJ3/AAV6s9C8JfEO30CX4oJ8Y/GdrcyG51yLUjq50u0Se5h/s6a8aWRnlEiCbbuYBbjOQWKjrP8AgnV+15rP7Cnxf8HfE7w/pWma1quh6Y8EVnqDOtvILi1MLEmMhsgNkc9RX0eRUZVYV6cd3HQ+cz+rGnKjUnspH7X/APBxr+wF8YP25Jvg4/wo8GS+Lh4VGt/2ps1Oysvsv2j+z/J/4+Zot+7yZfuZxs5xkZ/Mkf8ABAz9sAn/AJIxcnH/AFNGh/8AybX0f/xFefGAAj/hWHw4Of8Ap4vfx/jpw/4OvvjAP+aY/Dj/AMCL3/4uvVwVLNsNSVGnBNLz879zxsZUyrE1XWnNpvfT5Htf/Btzrus/sqfGP41fs0/EmxTwv8QtPubLxPDpUt3DcSS+ZaQidRJC7xMVhaxkwjE7ZW6bGA5v/grR8Uv29f2Xv2sdfl+H3iL4h618LfEM4vfDs3h/wta6tHpysq+ZZzbLSSSNo5dwXzCQ6FCGYhwv5o/tC/t2+N/jr+27q3x9sZh4G8daheWd9byaHM6rp0ttZQWamMvkkNHANytlWEjqwZSVr7z+C/8AwdcfEbwn4StrLxz8KvDHjPVYVCHU9O1mXRTOAMbpITBcKXOOSjIuScKBxVYjLMTGssUqcZuSXNF9HZXsPD5nhpUfqrnKCi3yyXVXPWv2YfgX/wAFI/2hvgvZ+Mdb+P6fDJb55JIdJ8S+G7OHUkt1xiaaMWWYdx3EJJhgACQM4FT/AINj/FWpeP8A9pj9q7W9a8QW/izVtVvdIuLzXbeFYodZkNzq+bpFVVVVlP7xQFX5WHy9cfJf7fP/AAcJ/F/9tb4f6j4L0jS9K+GHg7Womt9Tt9KupLzUdShYEPBJdsqbYXHDLFGjMMqzsjMh8n/4Jo/8FTfFv/BMDUfGtz4T8M+HPEbeN4rGK5XVZJoxbC0a5KeX5TDr9pfOc/dXHfLeVYmWGq80YxlK1orpr1YLM8NTxNNxk5RV7t6307HT/wDBf8Y/4K9/GNRkgyaOef8AsB6fmv14/wCDbkj/AIdM+D+S2dW1nn/uITV+CP7aH7VGr/tt/tNeKfilr2mado2reKzameysGdraH7PaQWq7S5LcpAGOT1YjpX03+wh/wXu+In7Av7OGmfDPw/4J8Ga9pWlXV3dx3eozXK3Dm4neZgdjBcBnIGB0xW+YZdXq5fSoRV5Ll09EcuAzGlSx1WtJ2jK9tO7Ptj/g2W+O2mr41/aH+GE9xFDq6eK5fFVnCzAPdQSObWdlGckRNDb7uOPtCevHyz/wWo/4JPfGTTf2/fGPi7wT8PfFXjjwl8R75dXsrzw/p0t+bW4kjUXEFwsYZoiJg7h3AjZHX5shlX4g+Ev7TfjT4CftBQfE7wXq8nh3xZa6hPqEU0A3xfvnZpIHRsiSFgxUo2cj3ANfpj4b/wCDs7xpZ+Dkt9X+C3hnUdfWLa19aeJJ7O0eTH3/ALM1vK6rn+HzicfxDrWVTAYzC4l4jDJS5lqn02/yN4Y7CYnDewxLcbPRn3Z/wQj/AGFfEv7B37D7aP41hWw8ZeMtZm8R6np/nJN/ZQeGGCK2LISpZYoEd9pIDyuAxABr5B/4Il/L/wAF3v2vFzz/AGj4l/8AUjFfP/w0/wCDnP46+Cte8U6jrHh7wZ4pl8R6it5bw3H2m3ttEgWJI1tLdEcnygVLkuWdnlcliNoXwv8AZN/4KxeMP2Rf2w/ib8ZtG8MeHdV1z4o3GoXF/p97JOLSzN5f/bXERVg2Ff5RuJyvvzXGspxsvbOoryml163T/A6ambYNOiqb0g+3Sx+gv7ehA/4Ogf2fyTwNF0v3/j1etj/g7Q5+AXwdGeP+Emuuf+3Nq/On4yf8FcPGfxo/4KDeCv2ib7wt4Zs/Evge0t7O00qCSc2NwsJuiC7MxfJN02cEfdX3zZ/4KTf8FhPGv/BTPwZ4X0PxV4T8L+HYPCt/LqEEulSTu8zyRGMq3mMRtxzxzmuuhlWIjXoVGtIRs9dtznr5th5Ua1OL1k7rTfY+jf8Ag1Iz/wANtfEUEMSPBJ7dP9Pt69w/bQ/aG0v9mX/g5o+FOv65dRWWhal4QstBvriQ7I7YXj6jBFIx6KqztCWY/KqbicAZH5nf8E4v+Civib/gmn8V9c8X+FvD+h+Ir3XtJ/seWDVHlSKKPzo5d6mMg7sxgc+tbnx/+OPjn/gth+3T4YL6V4P8NeLvFFhD4ZsLc3csGmuYRczpvkcOwdzIyDAPzbB3JrXFZbOeNqV5pckotXvtp+hjhcyhDB06MG+dSvtvr+p+uH/Bwv8A8Ey/HP7d3w98DeKvhnYx654s8AyXcE2jG4itpdSsrryWdonlKoZIngQ7GZQyySYJYKrcH/wbz/8ABJj4kfsdfEjxb8Uviro6+FtX1PSP+Ed0bR2vIbm5EEk8U9xPN5LOiBmt7dUXeW4k3Bfl3cB4l/an/bw/4I2fs/aGnxG0LwJ8UvAtsw0621V5rvUb3RAqr5Ud1cxeUfKYZVZJkckja0uSit2X/BGr9vb9oH/gpt+3df8AjbxpBHp3wr8H+GL22t7TR7KS10OPUri4tRGC8jM1xdeSkvzF2Eahtqx+aRJ4k1iYYKVFTi6avqnq9b2R7cfq88ZCq4yU30tovM8d/wCDjn4x6t+zx/wVW+Cfj3QQr6x4O8N2Wr2kTMUS4aHVLpzExH8EigofZjX6L/Hz4beAP+C3f/BNd7bw3rcMem+MLWLVNC1MxiWXQ9TgbKrLHn5XjkDwTR5B2tKoIJBH5Wf8HTXiqz1r/goX4Y022mjludE8DWiXYU7jE8t7eyBG9CE2t9JAe4r5K/Yf/wCCj3xa/wCCenim6v8A4ca/FBp2pSLLqWhajAbrSdTZVwHkh3KyvgAeZE8chVVUttGK76WVTr4KlWou04q689TzqmZwoYurSqK8JOz+6x13xA/4Iq/tR/Dvx5L4dm+D/iTWJ0lMcN9o7RXunXY3FVlWcMFRWAziXYygjcqniv1c/wCCWX/BCvwN+z7+y/fX/wC0X4I8BeKfGusXT6ndJqlvDfQ+GbRYlC2vnNlCy7XkkdDs3PgFwgdvn3Q/+DtnxJb6QkepfAnRr3UFUBprXxdLbQu2OSI2s5Coz23njv3r5V/b7/4LsfGj9vDwpe+Epm0vwD4E1BTHd6NoZkabUoz/AMs7q6ch5I+uY41iRgSrq4rarTzXFpUppQS3aZnSqZZhpOrBuUuiaPqL/gh7448EfET/AILtfGnWfhto2meHvAFz4P1WPQLLT4BBarZw6lo8KTJGAAiy+X52O3m9q3v+CvHiWz8J/wDBxn+zNf38wgtIdO8MJJI33Y9+u6pGrH0XcwyegGSeBX5yf8E6/wBvzxF/wTf+O+oeP/DOhaL4h1HUNCn0FrbVHlSFI5ri2naQGMg7wbZR6Ydvanf8FEv2/wDxJ/wUf+O+neP/ABNomj+HdR0zQrfQYrbSpJjCY4bi5nWTLsWDlrphxxhF96ueT1njOdfDy2vfysZxzaksJyt+9zXt87n7Wf8ABxt+yD49/a0/Y78Mf8K78P3vinVfCHiePVbvTLMB7uW1a1uYGeKPrIyvLGdi/NtLEA4xXjP/AAbVf8E7vib+zb4x8e/En4jeF9V8GRa5pcGiaPp2qR+RfXS+d500zwn54lUpEqhwGbLnaAFLeB/s0f8AB0n8UPhF8NrHQfHXgHRfiZfabCtvFrI1iTSLy5VVwGuR5E6Synu6CPd1IzknF1f/AIOgPjbffHl/Fdt4Y8JWvhmHS59NtPCrT3D2ySSSwSfa5p1KvNOohKKQqIqSvhckseCOAzGOHlg1Fcr63/A7p5jl7xEcW5PmXS34n0H+2+3/AB1EfAdhk40fTuBz/DqtfRf/AAcE/sB+Lv25v2U9En8AWK6x4v8AAGrnVIdMDKk2p2skLRTxQsxCiUExyAEjcImUZYrX47/F7/grl4z+MP8AwUJ8GftF3vhXwxaeJvBVrb2ltpcDzmxuVi+04LszeZk/an+6QPlX3z7h4x/4Odfjr4g+JfhTxBpugeDdDtfD4uYr/SIvtM9lr0U/k/LMGkBR4zDmORCGUu4O5WdG0nleMjOjUpJXhFJ3fXXQzhmmDlCrTqN2m77emp1P/BAj/glp8W9G/bq0T4nePPAvibwN4Z+HUV5NG2vWEmnTalezW0lrHFFDKBI6Ks8khkC7MxqAxJxXT/8AB198dNM8Q/Fn4TfDqynim1Hw3Y32u6mq8mAXbxRWyk9mIt52KnnBQ9GFQeP/APg7H8caz4JntPDfwb8NaDr80e1NRvfEU2o20Df3xbrbwlvYGUAd89D+W/xX+KviT45/ErW/GXjDWbzxB4o8R3RvNR1C6IMtxIQAOAAqqqqqKiqFRVVVUKqqO7B4LFV8YsXi0oqOiSOTGY7DUcI8Jhnzc27Ofooor6c+ZQUUUUAcmfgj4XJJOlDLdf8ASJv/AIqlHwT8MKoH9mcD/p4l/wDiq6uiuL+zcL/z7j9y/wAjt/tLF/8APyX3v/M5M/BHwuxBOlgkf9PE3/xVKnwT8MRsCNMwR/08Tf8AxVdXRR/ZuF/59x+5f5B/aWK/5+S+9/5nMf8ACm/DZAB008f9PEv/AMVQPg34bClTp3yt1/0iX/4qunoo/s3C/wDPtfcv8g/tLFf8/Jfe/wDM5i1+DnhyxuknhsZIbiJg6SR3UyujA5BBD5BB7iu38T+M/Efjnww+ia74s8Za7o7vvNjqXiG+vbfdnO4JLKyg55yBWfRR/ZuF/wCfcfuX+Qf2ni/+fkvvf+Zyg+CPhdWZhpa5Y7ji4l6/99V01naR6fZw28K7IbdFjjXJO1QMAZPPSpaK2o4ajRd6cFH0SX5GVbFVqqtVm5erb/MKKKK3OcKKKKACiiigNgoooouAUUUUXa2AKKKKACiiii4BVjRtYvPDmtWepadeXen6lptxHd2l3bSGKa1njYPHJGw5R1cKQw5BAPWq9FEkn7rQ1JrVM/W79lz/AIOpfEfhTwjZaP8AF74cx+L760hEb67oF4llPe4GAZbSRPLDkcs0ciqT0jUcDp/jV/wdgwL4auLT4Z/CC4t9TliZIL3xLqiLb2j/AMLG2twTMPVRNF/vV+NXXg84o6fh+leO8gwTnzcvyvp9x66z3FqPKpfO2v3nS/Gb4xeJv2g/inr3jbxlq9zrnijxNdG81C9lAUyuVCgBQAqIiKqIigKqqqgAACuaoor1oQUUoxVkuh5Mqjk3KWrYUUUVRNwooooHcKKKKBBRRRTbb3YBRRRSb7gFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFaHhHQj4p8WaXpgkWE6ldxWvmMQFTe4XcckDAznkge4q4xcmo99BTlypyey1Pd/2V/+CYHxV/au8AX/AI2sLbQ/B3w30tZWvfGXizUBpeiW/lhs4chpZRvXy8xRuquQrFa7n9mb/gjd4o/bMsdRm+Ffxb+CvjSXSH231rBf6tZ3tqm3Ima3utOhlaInCh0VgWOByGx9t/8ABzFqr/s6/su/A34N+EVXRvA8n2hp7K3yiTLZR26W8bY6qDK7nOcvtY8jNflf+yL+1p4x/Ym+OOnfEDwPc2sOuadDNb+XdxtLbXMUsZR45UDKWXkMBkYZFPavncLi8TjaM69GSitVHS97aa+u2lreZ7mLwtHByp0qsXJtJy1ta/RW7LXW9zzi6tns7qWF874nKN9QcGvdPjb/AME5fiT8AP2SPh98aPEEGmr4R+I77NPjhkma8s9ys8JuFaNUQTRozxlXfKjJx0rn/wBjb9nrUf2x/wBrDwn4ItYZ3HiLUvMv2t45Ha3tEzLcyAIrt8sSvj5Tzgd6/b74TeF/F3/BTb9g743fB74hfDnxL8PJNJvJLfwIuseHrnRYEsoxv0sx+bGNxheALIAWYIygn5gTpm2ZTwsINb6OX+HROy6tv8gy7L6WJrSjd8ruovzaurvyS19Ufz2W1rLe3McMMcs00zBERFLM7E4AAHJJPavqTVP+CUXiPwH4t8J+F/H/AMUvg58MvG/i62W6t/DniTVL9L2wRyfLF5Jb2c1ras6gMqyzKxDAEBsqPCfhv4q1P9m34/6DrlzpqtrHgLxBBey2FzwDPaXCu0L9cfNGVPXv1r9ZvjJ+z3+zR/wX68cL42+G/wAVbj4b/G7ULKKK/wDDeuWysdQMMMoQCBmUyOEiTdNayyokUal4g7Gtswxs6cadSN+R3vJK7Wmj66O+unSxjgcFGpOpTm0ppK0Xom72ae2qW3qfnf8AHX/gnJrv7M37XCfB3x74++G3hnWJLW3uRrVzdX7aMDPjy42lSzaSMnPLvEsagEs4HNd/+1n/AMEZPE37Df8AYR+KPxe+DXhg+JlmbTCG1+/F0ItnmHNtpcm3HmJ97Gd3GcHHEf8ABTn4N/G34HftH2eg/HS7h1fxHp+j2llpmr24ja21TToAYoHjlWONpdoUqWlUS5X5+cV+x/8AwUq/Yq8IftxfGL9lbwr4u8WaV4fsJbfV2lsJHuI9R12NLW0kMNmyxmFZFKgnzZEO1sqsm1lHn18wqwp0KntOaM+ZSaXRK6aVnr0Z3UMvpTq1qTpuMopNJvromm9NHumfjD+0d/wTy139nj9nHwn8V4/Hnw28eeDPGWoHTLK68L315cPDOIjKUnS4tYTC4VTmN8SKeCo5r5/rpvHet6loFzrHhC31XVP+EZsNZnuIdMa7drUTqWiE/lZ2eb5Y278bscZxXMoxRw3cHNe7g3NwvOXMnqtNUnbfuzxcZGMJunGNnHR63TaerV9bH0dH/wAE1PEfhn4aeC/E/wAQvHvw1+EsXxDYP4f0/wAVXl8NQvrdgmy8aKztLj7PbMWwJLgxj5SThcE+rv8A8EBfiyvxk03wbH44+D8zap4Sm8axa1HrV22kDTo5o4i5n+yZ+bzVcMFKbASXHAP1X4r1z9mT/gv34V8DW2r/ABAuvgz8ftD0uLRYLe9hQ2moZlizDEjskV0plklEMcU0U+ZGLRsqgV8pf8FCvhj+0/8A8E2bDR/h94z8Wwal4J1Pwzd+EtD1XS4IZLe90d7mO4nsDK8K3CEOIyUc5VSURmjJB8P6/iZ1PZc6hUbkuVrS2tmn1e3rrsewsDQVP2qi5wSi24vVO65k10VrpdtDivgl/wAEpLv9o/46T/DfwN8cvgd4m8YW/wBoJtrK415raVYP9Y8d0dLFvIgAyGSRlYcqWFWtL/4JGalq37Sl/wDCAfHP4D2vxE026NjLpV7fa1ZB7jcqiCKabTUhmlYuoVI5GZsnaDg49A/4Nsf+UoWh/wDYB1P/ANEivIf+Ctmq3Ohf8FSvjBfWc0lveWfil54JYzh4nUIysD2IIBronVxEcdHB+03g5N2W6lbTy6238znhToSwc8VybVFFK72avr5+ex6X8Gf+CCHxK+PXxF8a+D/DvxJ+DU3ir4eX76fr2lT6hqkFzZOHZUkAbT8SROF3K6FhhgDtbKj5s+O/7MUH7P8A+0FL8O9U+I3gDVbvT7o2Or6vpLalc6Xo06yNHJHMxs1lkMZXLG3ilHOASwZR+l//AAbU/GPxJ+0D+3L8avGfi7URq3iTxFolvc6heC2itvtEv2gKW8uJURSQBnaoyeepNfl7+1d/ydL8Sv8AsatU/wDSuWpw2JxX176tWle0E3ZddNnva97FYijh/qUsRSi177Su+lm1dd+h67+0x/wTIvv2UPB3gvXPFHxj+DFxa/ECCC+0VNLvNWvprixldFN6ypp/yQIr7yWw7CORY1kdSldx4x/4IieLvAf7L1t8aNT+MHwRT4Z3kUE0Ot295rV2jrNIIox5UOmtKG8xgjKU3IwIYKVOPH/2zLya78G/BjzpZJfK8CWcab2LbFDyYUZ6Aelfot8Q/wDlVD0D3mh/9SJqWNr4ijh4VFUu5VFHZbNv8VYrC4fD1a3I4WXs+fd7pKX3a7HxV4L/AOCOHxG+N/wXvPHHwj8XfDL40WmmuRe6V4U1a5XWLFMS/vJbO+trWVcmFgiY8yTKmNHByPJf2X/2Rr39p34zL8Pz4x8F+APFlzdjTrKz8XyX1iL27JdTbK8VrKscoZduyYxlnZUXcx212P8AwSZ/aE139m7/AIKCfDHV9Eu7iGPWdbtdB1OCOQql7Z3cyQyxuOjAblcA8B40PUA19M/8HNPwL0f4Oft2aF4u8PxjTrzx5oqanqKwfu83sErRGdcY2syLESRyWVm6sa3qYitRxUMNOV41L8rsrprdPo1bW9kY0sPSrYWdeEbSp2bV3ZpvTzT+bPn79vL/AIJTeKv+CdVnYp8QPiF8Mptc1a3N1p2i6TNqtze38QkSN3VmsEgQKTk+bKhIU7dx4p/wz/4JWan8Uf2VNR+M1t8Zfgpp3gbQ5Ft9Un1G91eC6026KI/2V4RpxeSb94oAhEgc52FxzX338ArrR/8Ag4c/4J3XHgXxTc22nfH74PxoNO165Ztt75i7Y55SqljHOIjHOAGKyRrIB8ypX5xftvfGvTLay0f4KeBVubT4c/C+4lid5CVk8S6zkpd6rOuBhmIMcSnJjhRRnLMK5cPisVKTwlSVqqlvZW5e68np53OmvhcMoxxcI/umrWu7qVtn89fReh8/XcK211LGk0dwsTlVljDBJAD94bgDg9eQD6gVHRRX0SPAk7u4UUUUCCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKdBO9tMksbMkkbBlYHBUg5BFNopqTTugeujP1p+O/wC1d8Jv+C3f7EXg/wAO+J/iH4X+E3x/+Hoe5RvFlx/Z2i6xiOOO52XhHkxpORG6oT5qPCyhGjHmH4v+C37MGifAvVrjx98VfG3wuj0nwt+/sPD+leI9I8X6h4mvvKleC2FrZy3MSQeZGnmyXe2IKwGJC22vmaivKp5b7HnhQlyxk27W2b3t2v53PSq5h7aMPbR5nFWvdq6WyffrtY/RP9jT4E6V8Jf2G/jR41t/ip8DtI+NPxF0ZdH8PaJJ490i1udM0yeVGvhnz/LhuJofkWNmVowpVijMVHG/8EDvihf/AAJ/bm0/xPc+MfAnhDwUtvNpniibxH4nsNKSa2kjd4xFHPKsk7ieKIgxKwU43FVbJ+HqKt4GTVXmlfnVttla1t/n66kvG6U7K3I7t33bafbTovQ/VP8Abp+F3wK8Jf8ABVrw58cbTx/8GvG/wb1/VodT8Y6baa9pusy2NwcRzltNieSe6jlYrKfKilIYylwoAJ8GH7GXhO8/bh0PxT8Jfjl8IbD4U3viFdd0rxBqfiy00PUPDEEd0ziGfTrySC8E0RjxGUhKSAxPuUM2z4lorPC5bUoRgoVG3FNarS3RNdbdHf5GmLzGGInNzppKdm7N3ulZtPpfd9z9Ff8AgsN+1V4f/wCCrn7c/hnw98NvEHhi08JeDtO+wJ4j8Satb6Fp1xJJKrXFx5t20f7pAY1CgGR/LkKI4Iz9a/8ABY34haD8YfCXwV8W/An49fBW8+IPwe1KWaCE+O9Dt5GE0UK+en2ucQNsa3GUkOGVzw2MV+GtFYPJIxp0qcJWVNtrS9297+T7epus6k6lWrUim5q3aysrJea7s+zvEv7Ffw6+Gv7AfxF+Inj34o/DTxJ8adTvrJvD/hvw3400/U7nT1e7C3Mk6WsrJK7o7NtiLpGqg7sllT5O+F99pul/Evw7c6yIm0i31O2lvhLEZozAsqmQMgB3DYDlcHI4wawqK9XC0Z0m3KV7tNK1klZKyXY8zFVo1YqMVbSzd7tu922z7f8A23/2UPhX+0R+0ve+Mv2c/id8HoPh34q1BUm07VtctvBz+E59sXmn7JqH2Z5LMly6NaxyYxJHsyg3ei/8F4f+CgnhL4++BvhZ8IPB/iqH4gH4b2/meIvFVvlrTVdRWFLfMEhP70fLLI0ilkbzU2s2DX5t0VwxypXpqc3KNN3V97+b626aLzudrzN+/KMFFzVna9rdbLo313P0I/4N5bDw/wDCv9rlPij41+IPw08EeGNJ028sEGu+LLCwvryeVEULHbSTCUIAd3mOqocEKWIIHlP/AAWa8EWKfty+OPG+geNPh9438L+OdUa/0+88NeJ7HVXjBRC0c0MMrSwsp4y6hG/hZsED5NorSeBlLGLGc2qXLa3S93879TGnjVHCPCcuknzXv1Wi+Xkfdv8AwQF/bz8C/sM/tT69cfEW+l0bw34u0f7ANUW3kuEsbhJVeMSrGGfy2G9dyq21imcLuZeX/a4/4J/DXv2wvFVx4V+MXwB13wZ4m1q41S38RP8AEjRreGxhuJnkKz25uDcl4w2GEMMu7jZuJ2j46op1cB/tP1qlK0rW2umvTTUVLGcuHlhakbxbT3s07d9dGj3/APbL8XeE/iz8Rvh14P8Ah3rFrrumeEvDeneFxrl1EuiWeq3gJ824BumTyYN7geZceWQFLMFHNfplr2g/D7xB/wAEDrH4Bn46/AZPiTZWCXy2Z8f6WsDXC6ib77J53nFPM2Ex7s+X5n8YT56/E6is8XlrrUY0VNrlalfS/MtV+b6GuGzL2VZ1nBP3eW2qVrJfkkff3/BMf9kf4d/AD42ab8X/AI9fGD4R+HNA+HV2up2mg6V4v0/xHq2qXUZQwSCDTpbgmJJGDkLukJixsCkuPKv+Cwn/AAUDtv8Agop+1zceK9Gs7mw8JaDZJouhx3A2zT26SSObiRf4WkeRjt/hUIDyDXytRWkcA5YhYmtK7Saitkr7vq7vvcj6/wAtCVCjGyk1zPdvql0SS9D9df8Ag3DvPB/7Jk3jnxn8R/ip8IfCVt4wsbGDS9PvfHGlC/dUMkjSSwictBjzFXZLtkBDZQYBP5y/tu/Cd/hT+0h4pii8SeC/Fum6vql3qGn6n4a8QWer2l1byTuyMTbyOYmweY5QjjrgggnySiphgJRxjxfNurWtpb/P/g6Dlj19U+q8vW979bfl5BRRRXpHnBRRRQAUUUUAFFFFABRRRQAUUUUAf//Z)

# **I work for a consumer finance company which specialises in lending various types of loans to urban customers. When the company receives a loan application, the company has to make a decision for loan approval based on the applicant’s profile. Two types of risks are associated with the bank’s decision:**
# 
# 
# 
# *  *If the applicant is likely to repay the loan, then not approving the loan results in a loss of business to the company*
# *  *If the applicant is not likely to repay the loan, i.e. he/she is likely to default, then approving the loan may lead to a financial loss for the company*
# 
# I "Mahipal Singh" herewith submitting one Ipython notebook which clearly explains the thought process behind my analysis (either in comments of markdown text), code, relevant plots and images.
# 
# 

# In[68]:


#Supress Warnings
import warnings
warnings.filterwarnings('ignore')


# In[69]:


##Importing relevant packages
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
get_ipython().run_line_magic('matplotlib', 'inline')


# In[70]:


##Read the dataset
url = "https://github.com/mahipal169/LendingClubCaseStudy/raw/master/loan/loan.csv"
df = pd.read_csv(url)
df.head()


# In[71]:


# Renaming the columns by removing leading and trailing whitespaces
df = df.rename(columns= lambda x: x.strip(), inplace=False)
df.describe()


# In[72]:


##Get the shape of the dataframe

df.shape


# # **Data Cleaning

# In[ ]:


#Removing all the Null values in the dataset


# In[74]:


df.dropna(axis = 1, how = 'all', inplace = True)
df.head()


# In[75]:


df.shape


# In[76]:


#There are columns with single valued they can not contribute therefore remove them


# In[77]:


df.drop(['pymnt_plan', "initial_list_status",'collections_12_mths_ex_med','policy_code','acc_now_delinq', 'application_type', 'pub_rec_bankruptcies', 'tax_liens', 'delinq_amnt'], axis = 1, inplace = True)
df.head()


# In[78]:


##Removing the columns that requires post approval of loan
df.drop(["id", "member_id", "url", "title", "emp_title", "zip_code", "last_credit_pull_d", "addr_state","desc","out_prncp_inv","total_pymnt_inv","funded_amnt", "delinq_2yrs", "revol_bal", "out_prncp", "total_pymnt", "total_rec_prncp", "total_rec_int", "total_rec_late_fee", "recoveries", "collection_recovery_fee", "last_pymnt_d", "last_pymnt_amnt", "next_pymnt_d" , "chargeoff_within_12_mths", "mths_since_last_delinq", "mths_since_last_record"], axis = 1, inplace = True)


# In[79]:


df.head()


# In[80]:


df.shape


# In[81]:


#getting the columns of the data
df.columns


# The goal of the analysis is to see who is likely to default and this can only be said in case of either fully paid or charged off loans.
# We cannot make anything up for the current loans. Therefore remove the records with current status

# In[82]:


df = df[df.loan_status != "Current"]
df.loan_status.unique()


# In[83]:


##Compute the percentage of missing values
(df.isna().sum()/len(df.index))*100


# Getting the type of data each column

# In[84]:


df.info()


# Get the employment length of the employees

# In[85]:


print("Mode : " + df.emp_length.mode()[0])
df.emp_length.value_counts()


# The Mode value is far higher than the other values so we can fill the Null Values with Mode values

# In[86]:


df.emp_length.fillna(df.emp_length.mode()[0], inplace = True)
df.emp_length.isna().sum()


# In[87]:


df.dropna(axis = 0, subset = ['revol_util'] , inplace = True)
df.revol_util.isna().sum()


# Convert the all the columns into Numeric data

# In[88]:


df.revol_util = pd.to_numeric(df.revol_util.apply(lambda x : x.split('%')[0]))


# In[89]:


df.int_rate = pd.to_numeric(df.int_rate.apply(lambda x : x.split('%')[0]))


# In[90]:


df.emp_length = pd.to_numeric(df.emp_length.apply(lambda x: 0 if "<" in x else (x.split('+')[0] if "+" in x else x.split()[0])))


# In[91]:


df.head()


# In[92]:


df.emp_length.value_counts()


# Analyze the The self-reported annual income provided by the borrower during registration.

# In[93]:


sns.boxplot(df['annual_inc'])


# In[95]:


#Checking % of NaNs in columns (>0)
missing_val_cols_prcnt = round(100*df.isnull().sum()/len(df.index),4)
missing_val_cols_prcnt[missing_val_cols_prcnt!=0]


# Remove the Outliers

# In[96]:


quantile_info = df.annual_inc.quantile([0.5, 0.75,0.90, 0.95, 0.97,0.98, 0.99])
quantile_info


# In[97]:


per_95_annual_inc = df['annual_inc'].quantile(0.95)
df = df[df.annual_inc <= per_95_annual_inc]


# In[98]:


sns.boxplot(df.annual_inc)


# In[99]:


sns.boxplot(df.funded_amnt_inv)


# In[100]:


##Visualize the categorical data of fully paid and charged-off
sns.countplot(x = 'loan_status', data = df)


# In[101]:


df['sub_grade'] = df['sub_grade'].str.extract('(\d+)$').astype(float)


# In[102]:


df.sub_grade.head()


# ##visualize the distribution of 'sub_grade' within each 'grade' category for loans with the status 'Charged Off'.

# In[103]:


plt.figure(figsize=(11, 6))
sns.set_palette('colorblind')
sns.countplot(x='grade', order=['A', 'B', 'C', 'D', 'E', 'F', 'G'], hue='sub_grade', data=df[df['loan_status'] == 'Charged Off'], palette='tab10')
plt.show()


# In[104]:


#Analyze the ownership of home


# In[105]:


df['home_ownership']


# In[106]:


df['home_ownership'].unique()


# In[107]:


plt.figure(figsize=(6, 4))
sns.countplot(x='home_ownership', data=df[df['loan_status'] == 'Charged Off'], log=True)
plt.show()


# Analyze the pupose of Loans 

# In[108]:


plt.figure(figsize=(12, 8))
sns.countplot(y='purpose', data=df[df['loan_status'] == 'Charged Off'], ax=plt.gca(), log=True)
plt.show()


# In[ ]:


# Create the bins for numerical variable to make it categorical


# In[109]:


# Dictionary containing column names and bin ranges
columns_bins = {
    'int_rate': [5, 9, 13, 17, 21, 24],
    'open_acc': [2, 10, 19, 27, 36, 44],
    'revol_util': [0, 20, 40, 60, 80, 100],
    'total_acc': [2, 20, 37, 55, 74, 90],
    'annual_inc': [3000, 31000, 58000, 85000, 112000, 140000]
}

# Loop over dictionary items to create new groups
for column, bins in columns_bins.items():
    new_column_name = f'{column}_groups'
    df[new_column_name] = pd.cut(df[column], bins=bins, precision=0)

df.head()


# In[ ]:


# Analysing wrt interest rate bins


# In[140]:


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 8))

sns.countplot(x='int_rate_groups', data=df[df['loan_status'] == 'Charged Off'], ax=axes[0])
axes[0].set_xlabel('Interest Rate')

sns.countplot(x='emp_length', data=df[df['loan_status'] == 'Charged Off'], ax=axes[1])

plt.show()


# In[141]:


##Analyze the open account groups
fig, ax = plt.subplots(figsize=(7, 4))
sns.countplot(x='open_acc_groups', data=df[df['loan_status'] == 'Charged Off'], ax=ax)
ax.set_xlabel('open_acc_groups')
plt.show()


# In[117]:


##Analyze the open account groups
fig, ax = plt.subplots(figsize=(7, 5))
sns.countplot(x='revol_util_groups', data=df[df['loan_status'] == 'Charged Off'], ax=ax)
ax.set_xlabel('revol_util_groups')
plt.show()


# In[118]:


fig, ax = plt.subplots(figsize=(7, 5))
sns.countplot(x='total_acc_groups', data=df[df['loan_status'] == 'Charged Off'], ax=ax)
ax.set_xlabel('total_acc_groups')
plt.show()


# In[150]:


fig, ax = plt.subplots(figsize=(8, 4))
sns.countplot(x='annual_inc_groups', data=df[df['loan_status'] == 'Charged Off'], ax=ax)
ax.set_xlabel('annual_inc_groups')
plt.show()


# In[123]:


sns.countplot(y='term', data=df[df['loan_status']=='Charged Off'])


# In[124]:


sns.countplot(x='verification_status', data=df[df['loan_status']=='Charged Off'])


# In[125]:


plt.figure(figsize=(10, 8))
sns.countplot(x='inq_last_6mths', data=df[df['loan_status'] == 'Charged Off'], log=True)
plt.show()


# In[126]:


plt.figure(figsize=(10, 8))
sns.countplot(x='pub_rec', data=df[df['loan_status'] == 'Charged Off'], log=True)
plt.show()


# In[ ]:


#Analyze by months and year


# In[127]:


df[['issue_month', 'issue_year']] = df['issue_d'].str.split('-', expand=True)

# Adding '20' to the year column
df['issue_year'] = '20' + df['issue_year']


# In[128]:


df.head()


# In[130]:


fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15, 15))

sns.countplot(x='issue_month', data=df[df['loan_status'] == 'Charged Off'], ax=axes[0])
sns.countplot(x='issue_year', data=df[df['loan_status'] == 'Charged Off'], ax=axes[1])

plt.tight_layout()
plt.show()


# In[ ]:


# Analysing installment, dti and loan amount


# In[131]:


# Dictionary containing column names and bin ranges
columns_bins = {
    'installment': (14, 145, 274, 403, 531, 660, 789, 918, 1047, 1176, 1305),
    'funded_amnt_inv': (0, 5000, 10000, 15000, 20000, 25000, 30000, 35000),
    'loan_amnt': (0, 5000, 10000, 15000, 20000, 25000, 30000, 35000),
    'dti': (0, 6, 12, 18, 24, 30)
}

# Loop over dictionary items to create new groups
for column, bins in columns_bins.items():
    new_column_name = f'{column}_groups'
    df[new_column_name] = pd.cut(df[column], bins=bins, precision=0)

df.head()


# In[133]:


plt.figure(figsize=(12, 5))
sns.countplot(x='funded_amnt_inv_groups', data=df[df['loan_status'] == 'Charged Off'], log=True)
plt.show()


# In[134]:


plt.figure(figsize=(12, 5))
sns.countplot(x='loan_amnt_groups', data=df[df['loan_status'] == 'Charged Off'], log=True)
plt.show()


# In[136]:


sns.countplot(x='dti_groups', data=df[df['loan_status']=='Charged Off'])


# In[137]:


plt.figure(figsize=(12, 5))
sns.countplot(x='installment_groups', data=df[df['loan_status'] == 'Charged Off'], log=True)
plt.show()


# In[151]:


#Annual Income vs Purpose of the loan


# In[158]:


plt.figure(figsize=(8,8))
sns.barplot(data =df,x='annual_inc', y='purpose', hue ='loan_status',palette="deep")
plt.show()


# In[159]:


##Annual Income Vs home ownership


# In[161]:


plt.figure(figsize=(10,10))
sns.barplot(data =df,x='home_ownership', y='annual_inc', hue ='loan_status',palette="pastel")
plt.show()


# In[166]:


##Annual Income Vs Loan Amount
plt.figure(figsize=(8,5))
sns.barplot(x = "annual_inc_groups", y = "loan_amnt", hue = 'loan_status', data = df)
plt.show()


# In[169]:


##Annual Income Vs interest rates
plt.figure(figsize=(8,5))
sns.barplot(data =df,x='int_rate_groups', y='annual_inc', hue ='loan_status',palette="pastel")
plt.show()


# In[176]:


##Analysis loan Amount vs intertest rates
plt.figure(figsize=(10,8))
sns.barplot(data =df,x='loan_amnt_groups', y='int_rate', hue ='loan_status',palette="pastel")
plt.show()


# In[178]:


#Loan Amount and Purpose of loan
plt.figure(figsize=(10,10))
sns.barplot(data =df,x='loan_amnt', y='purpose', hue ='loan_status',palette="pastel")
plt.show()


# In[187]:


plt.figure(figsize=(20,20))
plt.subplot(221)
sns.lineplot(data =df,y='loan_amnt', x='issue_month', hue ='loan_status',palette="pastel")
plt.subplot(222)
sns.lineplot(data =df,y='loan_amnt', x='issue_year', hue ='loan_status',palette="pastel")


# In[188]:


plt.figure(figsize=(20,20))
plt.subplot(221)
sns.barplot(data =df,y='loan_amnt', x='emp_length', hue ='loan_status',palette="pastel")
plt.subplot(222)
sns.barplot(data =df,y='loan_amnt', x='verification_status', hue ='loan_status',palette="pastel")


# In[190]:


plt.tight_layout()
sns.catplot(data =df,y ='int_rate', x ='loan_amnt_groups', hue ='loan_status',palette="pastel",kind = 'box')


# In[193]:


sns.catplot(x = 'term', y = 'loan_amnt', data = df,hue = 'loan_status', kind = 'bar')


# In[ ]:





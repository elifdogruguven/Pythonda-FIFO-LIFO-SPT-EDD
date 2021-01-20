#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PROGRAMI TEKRAR ÇALIŞTIRMAK İÇİN GEREKLİ KOD
while True:
  #KULLANICIDAN MAKİNE SAYISI VE İŞ SAYISI DEĞERİ ALINACAK
  makinesayisi=int(input('Makine sayısını giriniz...'))
  print('Makine sayısı= {}'.format(makinesayisi))
  issayisi= int(input('iş sayısını giriniz...'))
  print('İş sayısı={}'.format(issayisi))
    
    
  # listeyi oluşturma
  isIsimList = []
  isPTList = []
  isDDList = []
  # kullanıcıdan değer alma
  for i in range(issayisi):
    # Otomatik olarak işe A'dan Z'ye isim verme (ASCII kod ile)
    isIsimList.append(chr(65+i))
    # X isimli iş için kullanıcıdan işlem süresi alma
    isPTList.append(int(input(str(chr(65+i)) + ". işin işlem süresini giriniz:  ")))
    # X isimli iş için kullanıcıdan işlem süresi alma
    isDDList.append(int(input(str(chr(65+i)) + ". işin teslim süresini giriniz: ")))
      
  # liste elemanlarını yazdırma
  print("İş isimleri: ")
  print(isIsimList)
  
  print("İşlem süreleri: ")
  print(isPTList)
  
  print("Teslim süreleri: ")
  print(isDDList)
    
  while True:
    # is sırası seçimi
    a=str(input("İş sırasını seçiniz. fifo/lifo/spt/edd"))
    print("İş sırası:", end = ' ')
    if a=="fifo":
      for i in range(issayisi): 
        print(isIsimList[i], end = ' ')
      print("")
        
    if a=="lifo":
      for i in range(issayisi): 
        print(isIsimList[(len(isIsimList)-i-1)], end =' ')
      print("")
      
    if a=="spt":
      kopya_isPTList = isPTList.copy()
      kopya2_isPTList = isPTList.copy()
      kopya_isPTList.sort()
      for i in range(issayisi): 
        for j in range(issayisi): 
          if kopya_isPTList[i] == kopya2_isPTList[j]:
            kopya2_isPTList[j] = -1
            print(isIsimList[j], end =' ')
      print("")
      
    if a=="edd":
      kopya_isDDList = isDDList.copy()
      kopya2_isDDList = isDDList.copy()
      kopya_isDDList.sort()
      for i in range(issayisi): 
        for j in range(issayisi): 
          if kopya_isDDList[i] == kopya2_isDDList[j]:
            kopya2_isDDList[j] = -1
            print(isIsimList[j], end =' ')
      print("")  
      
    answer = str(input('Sıralama tekrar çalıştırılsın mı? (e/h): '))
    if answer == "e":
      continue
    elif answer == "h":
      break
    else:
      print("Yanlış karakter. Çıkış yapılıyor.")
      break
  answer = str(input('Program tekrar çalıştırılsın mı? (e/h): '))
  if answer == "e":
    continue
  elif answer == "h":
    print('Kullandığınız için teşekkür ederiz.') 
    print('2020™ TÜM HAKLARI SAKLIDIR®.')
    break
  else:
    print("Yanlış karakter. Çıkış yapılıyor.")
    print('Kullandığınız için teşekkür ederiz.') 
    print('2020™ TÜM HAKLARI SAKLIDIR®.')
    break


# In[ ]:





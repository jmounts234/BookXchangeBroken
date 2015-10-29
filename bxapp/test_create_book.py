from  helpers import createbook

# valid 9780553293357

def test_valid_isbn():
  book = createbook("9780553293357")
  if book.validate_isbn(): return True 
  return False

def test_invalid_isbn_too_short():
  book = createbook("97805532")
  if not book.validate_isbn(): return True 
  return False

def test_invalid_isbn_numericity():
  book = createbook("978055asdfd12")
  if not book.validate_isbn(): return True 
  return False

def test_invalid_isbn_zeros():
  book = createbook("0000000000001")
  if not book.validate_isbn(): return True 
  return False

def test_api_link_generator():
  book = createbook("9780553293357")
  if book.gen_url() == "https://www.googleapis.com/books/v1/volumes?q=isbn:9780553293357": return True
  return False

def test_get_rawjson():
  book = createbook("9780553293357")
  try:
    if book.get_rawjson()[0:100] == "insert json": 
      return True
  except:
    return False

results = {
  "test_valid_isbn" : test_valid_isbn(),
  "test_invalid_isbn_too_short" : test_invalid_isbn_too_short(),
  "test_invalid_isbn_numericity" : test_invalid_isbn_numericity(),
  "test_invalid_isbn_zeros" : test_invalid_isbn_zeros(),
  "test_api_link_generator" : test_api_link_generator(),
  "test_get_rawjson" : test_get_rawjson()
}

passed = 0
failed = 0
for k in results.keys():
  if results[k]: 
    passed += 1
  else: 
    failed += 1
    print(str(k) + " FAILED")
print("----------------------------")
print("passed = " + str(passed) + ", failed = " + str(failed))
print("----------------------------")




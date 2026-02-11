import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

train_set_processed = train_set
val_set_processed = val_set

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Customized stop words list from NLTK, removing certain pronouns and verbs that could be considered PCL
custom_stop_words = set(stopwords.words('english')) - {'i', 'their', 'ourselves', 'need', 'should', 'must', 'us','them','we','they'}

# Function to preprocess text according to the provided specifications
def preprocess_text(text):
    # White-space normalization
    text = ' '.join(text.split())
    
    # B Punctuation normalization (and removal)
    # text = re.sub(r'[^\w\s]', '', text)
    
    # Lowercasing
    text = text.lower()
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # C Replace stop words with a standardized token (Here, I'm simply removing the stop words)
    # tokens = [word for word in tokens if word not in custom_stop_words]
    
    # D Substitute numbers with a numeric token <num>
    tokens = ['<num>' if word.isdigit() else word for word in tokens]
    
    # Stemming and lemmatization
    # tokens = [stemmer.stem(lemmatizer.lemmatize(word)) for word in tokens]
    
    # Re-join tokens into a single string
    text = ' '.join(tokens)
    return text

# Apply the preprocessing function to the text columns
train_set_processed['text'] = train_set_processed['text'].apply(preprocess_text)
val_set_processed['text'] = val_set_processed['text'].apply(preprocess_text)

# Assuming train_set and val_set are defined somewhere in the code with 'text' column

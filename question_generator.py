import re
import random
from typing import List, Dict, Any
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

class QuestionGenerator:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        
    def generate_questions(self, content: str, requirements: Dict[str, Any]) -> Dict[str, List[Dict]]:
        """
        Generate different types of questions based on content and requirements
        """
        # Split content into sentences and paragraphs
        sentences = sent_tokenize(content)
        paragraphs = self._split_into_paragraphs(content)
        
        # Extract key concepts and terms
        key_terms = self._extract_key_terms(content)
        
        questions = {
            'mcq': [],
            'short_answer': [],
            'long_answer': []
        }
        
        # Generate MCQ questions (1 mark)
        for i in range(requirements['mcq_count']):
            mcq = self._generate_mcq(sentences, key_terms, requirements['difficulty'])
            if mcq:
                questions['mcq'].append(mcq)
        
        # Generate short answer questions (2 marks)
        for i in range(requirements['short_answer_count']):
            short_q = self._generate_short_answer(sentences, paragraphs, requirements['difficulty'])
            if short_q:
                questions['short_answer'].append(short_q)
        
        # Generate long answer questions (5 marks)
        for i in range(requirements['long_answer_count']):
            long_q = self._generate_long_answer(paragraphs, content, requirements['difficulty'])
            if long_q:
                questions['long_answer'].append(long_q)
        
        return questions
    
    def _split_into_paragraphs(self, content: str) -> List[str]:
        """Split content into meaningful paragraphs"""
        paragraphs = content.split('\n\n')
        return [p.strip() for p in paragraphs if len(p.strip()) > 50]
    
    def _extract_key_terms(self, content: str) -> List[str]:
        """Extract important terms and concepts from content"""
        words = word_tokenize(content.lower())
        words = [word for word in words if word.isalpha() and word not in self.stop_words]
        
        # Get POS tags to identify nouns and adjectives
        pos_tags = pos_tag(words)
        key_terms = [word for word, pos in pos_tags if pos in ['NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS']]
        
        # Count frequency and return most common terms
        term_freq = {}
        for term in key_terms:
            term_freq[term] = term_freq.get(term, 0) + 1
        
        return sorted(term_freq.keys(), key=lambda x: term_freq[x], reverse=True)[:20]
    
    def _generate_mcq(self, sentences: List[str], key_terms: List[str], difficulty: str) -> Dict[str, Any]:
        """Generate Multiple Choice Question"""
        if not sentences or not key_terms:
            return None
        
        # Select a sentence that contains key terms
        relevant_sentences = [s for s in sentences if any(term in s.lower() for term in key_terms[:10])]
        if not relevant_sentences:
            relevant_sentences = sentences
        
        sentence = random.choice(relevant_sentences)
        
        # Create question based on sentence
        question_patterns = [
            "What is the main topic discussed in the following statement?",
            "According to the text, which of the following is true?",
            "What does the following statement imply?",
            "Which concept is being described in the given text?"
        ]
        
        question = random.choice(question_patterns)
        
        # Generate options
        correct_answer = self._extract_key_concept(sentence)
        if not correct_answer:
            return None
        
        # Generate distractors
        distractors = self._generate_distractors(key_terms, correct_answer)
        
        options = [correct_answer] + distractors[:3]
        random.shuffle(options)
        
        return {
            'question': f"{question}\n\n\"{sentence}\"",
            'options': options,
            'correct_answer': correct_answer,
            'marks': 1,
            'difficulty': difficulty
        }
    
    def _generate_short_answer(self, sentences: List[str], paragraphs: List[str], difficulty: str) -> Dict[str, Any]:
        """Generate Short Answer Question (2 marks)"""
        if not sentences:
            return None
        
        # Select a sentence for question generation
        sentence = random.choice(sentences)
        
        question_patterns = [
            "Explain briefly:",
            "What is meant by:",
            "Define:",
            "Describe:",
            "What are the key points about:"
        ]
        
        # Extract key concept from sentence
        key_concept = self._extract_key_concept(sentence)
        if not key_concept:
            return None
        
        question = f"{random.choice(question_patterns)} {key_concept}"
        
        # Generate sample answer
        sample_answer = self._generate_sample_answer(sentence, key_concept)
        
        return {
            'question': question,
            'sample_answer': sample_answer,
            'marks': 2,
            'difficulty': difficulty
        }
    
    def _generate_long_answer(self, paragraphs: List[str], content: str, difficulty: str) -> Dict[str, Any]:
        """Generate Long Answer Question (5 marks)"""
        if not paragraphs:
            return None
        
        paragraph = random.choice(paragraphs)
        
        question_patterns = [
            "Discuss in detail:",
            "Analyze and explain:",
            "Compare and contrast:",
            "Evaluate the following:",
            "Critically examine:"
        ]
        
        # Extract main topic from paragraph
        main_topic = self._extract_main_topic(paragraph)
        if not main_topic:
            return None
        
        question = f"{random.choice(question_patterns)} {main_topic}"
        
        # Generate detailed answer
        detailed_answer = self._generate_detailed_answer(paragraph, main_topic, content)
        
        return {
            'question': question,
            'detailed_answer': detailed_answer,
            'marks': 5,
            'difficulty': difficulty
        }
    
    def _extract_key_concept(self, sentence: str) -> str:
        """Extract key concept from a sentence"""
        words = word_tokenize(sentence)
        pos_tags = pos_tag(words)
        
        # Look for nouns and adjectives
        key_words = [word for word, pos in pos_tags if pos in ['NN', 'NNS', 'NNP', 'NNPS', 'JJ']]
        
        if key_words:
            return random.choice(key_words).capitalize()
        return None
    
    def _extract_main_topic(self, paragraph: str) -> str:
        """Extract main topic from a paragraph"""
        sentences = sent_tokenize(paragraph)
        if not sentences:
            return None
        
        # Use the first sentence to extract topic
        first_sentence = sentences[0]
        words = word_tokenize(first_sentence)
        pos_tags = pos_tag(words)
        
        # Find the main noun phrase
        main_words = [word for word, pos in pos_tags if pos in ['NN', 'NNS', 'NNP', 'NNPS']]
        
        if main_words:
            return ' '.join(main_words[:3]).capitalize()
        return None
    
    def _generate_distractors(self, key_terms: List[str], correct_answer: str) -> List[str]:
        """Generate distractor options for MCQ"""
        # Remove correct answer from key terms
        other_terms = [term for term in key_terms if term.lower() != correct_answer.lower()]
        
        # Select random terms as distractors
        distractors = random.sample(other_terms, min(3, len(other_terms)))
        return [term.capitalize() for term in distractors]
    
    def _generate_sample_answer(self, sentence: str, key_concept: str) -> str:
        """Generate sample answer for short answer question"""
        return f"Based on the text, {key_concept.lower()} refers to the concept mentioned in the context: '{sentence[:100]}...'"
    
    def _generate_detailed_answer(self, paragraph: str, main_topic: str, content: str) -> str:
        """Generate detailed answer for long answer question"""
        return f"""The {main_topic.lower()} is a significant concept that can be analyzed from multiple perspectives:

1. Definition and Context: {paragraph[:200]}...

2. Key Characteristics: The main aspects include various elements that contribute to understanding this topic.

3. Implications: This concept has important implications for the broader context discussed in the document.

4. Conclusion: Understanding {main_topic.lower()} is crucial for comprehending the overall subject matter."""

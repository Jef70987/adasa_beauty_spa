// Admin state
let isAdmin = false;
fetch('/api/data/')
// Sample feedback data
let feedbackData = [
    {
        id: 1,
        name: "Emma Johnson",
        service: "Massage Therapy",
        rating: 5,
        comment: "The aromatherapy massage was heavenly! The therapist listened to my needs and the ambiance was so relaxing. Will definitely come back!",
        date: "2023-06-15",
        reply: "Dear Emma, we're thrilled you enjoyed your massage! Our lavender essential oil is a guest favorite. See you again soon! 💐"
    },
    {
        id: 2,
        name: "Carlos Mendez",
        service: "Facial Treatment",
        rating: 1,
        comment: "Great deep cleansing facial, though I wish the extraction part was a bit gentler. Skin feels amazing though!",
        date: "2023-06-12",
        reply: "Hi Carlos, thank you for your feedback! We'll adjust the pressure during extractions on your next visit. So glad your skin is happy!"
    }
];

// DOM Elements
const feedbackForm = document.getElementById('feedbackForm');
const feedbackContainer = document.getElementById('feedbackContainer');
const adminToggle = document.getElementById('adminToggle');
const ratingStars = document.getElementById('ratingStars').children;
const ratingValue = document.getElementById('ratingValue');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    renderFeedback();
    setupRatingStars();
    
    // Form submission
    feedbackForm.addEventListener('submit', function(e) {
        e.preventDefault();
        handleFormSubmit();
    });
    
    // Admin toggle
    adminToggle.addEventListener('click', toggleAdminMode);
});

// Rating stars interaction
function setupRatingStars() {
    for (let star of ratingStars) {
        star.addEventListener('click', function() {
            const value = this.getAttribute('data-value');
            ratingValue.value = value;
            
            // Update star display
            for (let i = 0; i < ratingStars.length; i++) {
                if (i < value) {
                    ratingStars[i].classList.add('active');
                } else {
                    ratingStars[i].classList.remove('active');
                }
            }
        });
    }
}

// Handle form submission
function handleFormSubmit() {
    const newFeedback = {
        id: Date.now(),
        name: document.getElementById('clientName').value,
        service: document.getElementById('serviceType').value,
        rating: parseInt(ratingValue.value),
        comment: document.getElementById('feedbackText').value,
        date: new Date().toLocaleDateString('en-US', { 
            year: 'numeric', 
            month: 'short', 
            day: 'numeric' 
        }),
        reply: ""
    };
    
    feedbackData.unshift(newFeedback);
    renderFeedback();
    feedbackForm.reset();
    
    // Reset stars
    for (let star of ratingStars) {
        star.classList.remove('active');
    }
    ratingValue.value = "";
}

// Toggle admin mode
function toggleAdminMode() {
    isAdmin = !isAdmin;
    adminToggle.textContent = isAdmin ? '0~' : 'O~';
    adminToggle.style.backgroundColor = isAdmin ? '#fb084' : '#b91b7c';
    renderFeedback();
}

// Render all feedback
function renderFeedback() {
    if (feedbackData.length === 0) {
        feedbackContainer.innerHTML = `
            <div class="empty-state">
                <img src="https://cdn-icons-png.flaticon.com/512/2491/2491908.png" alt="Empty feedback">
                <p>No feedback yet. Be the first to share!</p>
            </div>
        `;
        return;
    }
    
    feedbackContainer.innerHTML = '';
    
    feedbackData.forEach(feedback => {
        const feedbackCard = document.createElement('div');
        feedbackCard.className = 'feedback-card';
        
        // Create rating stars
        let starsHtml = '';
        for (let i = 0; i < 5; i++) {
            starsHtml += i < feedback.rating ? '★' : '☆';
        }
        
        feedbackCard.innerHTML = `
            <div class="feedback-header">
                <div>
                    <span class="client-name">${feedback.name}</span>
                    <span class="service-name"> - ${feedback.service}</span>
                </div>
                <div class="feedback-date">${feedback.date}</div>
            </div>
            
            <div class="feedback-rating" title="${feedback.rating} out of 5 stars">
                ${starsHtml}
            </div>
            
            <div class="feedback-content">
                ${feedback.comment}
            </div>
            
            ${feedback.reply ? `
                <div class="admin-reply">
                    ${feedback.reply}
                </div>
            ` : ''}
            
            ${isAdmin ? `
                <div class="admin-controls">
                    <button 
                        onclick="toggleReplyForm(${feedback.id})" 
                        class="btn" 
                        style="padding: 8px 15px; font-size: 14px; background-color:purple;">
                        ${feedback.reply ? 'Edit Reply' : 'Add Reply'}
                    </button>
                </div>
                
                <div id="replyForm-${feedback.id}" class="reply-form">
                    <textarea 
                        id="replyText-${feedback.id}" 
                        placeholder="Write your spa response..."
                        rows="3">${feedback.reply || ''}</textarea>
                    <button 
                        onclick="submitReply(${feedback.id})" 
                        class="btn" 
                        style="margin-right: 10px; padding: 8px 15px; font-size: 14px;">
                        Submit
                    </button>
                    <button 
                        onclick="toggleReplyForm(${feedback.id})" 
                        style="padding: 8px 15px; font-size: 14px; background:rgb(250, 13, 222); border: 1px solid purple;">
                        Cancel
                    </button>
                </div>
            ` : ''}
        `;
        
        feedbackContainer.appendChild(feedbackCard);
    });
}

// Admin reply functions
function toggleReplyForm(feedbackId) {
    const form = document.getElementById(`replyForm-${feedbackId}`);
    form.style.display = form.style.display === 'block' ? 'none' : 'block';
}

function submitReply(feedbackId) {
    const replyText = document.getElementById(`replyText-${feedbackId}`).value.trim();
    if (replyText) {
        const feedback = feedbackData.find(f => f.id === feedbackId);
        if (feedback) {
            feedback.reply = replyText;
            renderFeedback();
        }
    }
}
// Make functions available globally for inline handlers
window.toggleReplyForm = toggleReplyForm;
window.submitReply = submitReply;

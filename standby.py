# 6. Mode & Settings Selection Tabs
tab_game, tab_settings = st.tabs(["🎴 Flashcard Game", "⚙️ Game Settings"])

# --- TAB 1: SETTINGS ---
with tab_settings:
    st.subheader("⚙️ Custom Game Settings")
    st.write("Customize how you want to study your ETK vocabulary:")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        show_pinyin_setting = st.toggle("Show Pinyin automatically", value=True)
        enable_hints = st.toggle("Enable sentence hints", value=True)
    with col_s2:
        game_mode = st.radio("Study Mode:", ["Standard Flashcard", "Dictation Challenge"])

# --- TAB 2: FLASHCARD GAME ---
with tab_game:
    # Stats Summary Row
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Unit", value=selected_unit)
    with m2:
        st.metric(label="Total Words", value=num_words)
    with m3:
        st.metric(label="Streak", value="🔥 5")
    
    st.write("")
    
    # Word Index Selector
    if num_words > 1:
        word_index = st.slider("Navigate Words:", 0, num_words - 1, 0)
    else:
        word_index = 0

    current_word = filtered_df.iloc[word_index]

    # Main Flashcard Box (Rounded & Bordered)
    with st.container(border=True):
        st.caption(f"CARD {word_index + 1} OF {num_words}")
        st.markdown("### 🔤 English Definition:")
        st.title(current_word['English'])
        
        st.divider()
        
        # Interactive Rounded Action Buttons
        b_col1, b_col2 = st.columns(2)
        
        with b_col1:
            reveal = st.button("👁️ Reveal Answer", use_container_width=True)
        with b_col2:
            next_word = st.button("✨ Next Word", use_container_width=True)
            
        if reveal:
            st.success(f"**Chinese Character:** {current_word['CHARACTER']}")
            
            if show_pinyin_setting:
                st.info(f"**Pinyin:** {current_word['Pinyin']}")
                
            if enable_hints:
                st.write(f"**Sentence:** {current_word['Sentence']}")